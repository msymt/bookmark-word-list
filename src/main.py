import json
import getpass
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# get dictionary-type data of your bookmarks
def get_chrome_bookmark_data(path) -> dict:
    with open(path) as f:
        return json.load(f)

# define a function that extracts a url from each bookmark
def get_weblio_url(bookmark):
    if 'Weblio' in bookmark['name'] and '意味・' in bookmark['name']:
        return bookmark['url']

def extract_words_meanings_from_html_files(df: pd.DataFrame, url_list_filtered: list):
    i = 0
    while i < len(url_list_filtered):
        # analyse html files
        response = requests.get(url_list_filtered[i])
        soup = BeautifulSoup(response.content, "html.parser")    
        # extract meanings by setting the class
        elements = soup.select(".content-explanation.ej")
        # extract only alphabets from the title, which is the word
        alphabet = re.compile('[a-z,A-Z]+')
        word = ' '.join(alphabet.findall(soup.title.text)).replace('Weblio', '')
        # store the words and meanings in a dataframe
        if len(elements) > 0:
            df = df.append([[word, elements[0].text]], ignore_index=True)
        i += 1
    return df

def main():
    # set a PATH to your bookmark repository
    # if you use other os, please modify PATH
    CHROME_BOOKMARK_PATH = (
        '/Users/{username}/Library/Application Support/'
        'Google/Chrome/Default/Bookmarks'
    ).format(username=getpass.getuser())

    #### get bookmark info ####
    bookmark_data = get_chrome_bookmark_data(CHROME_BOOKMARK_PATH)

    # locate your wanted bookmarks /////This depends on the structure of your bookmarks.
    folderLocationNumber = 0
    bookmarks = bookmark_data['roots']['bookmark_bar']['children'][folderLocationNumber]['children']

    ### get the urls of the bookmarks ####
    # apply the function to the whole bookmarks
    url_list = list(map(get_weblio_url,bookmarks))
    print(url_list)

    # filter out None from the url list.
    url_list_filtered = list(filter(None, url_list))

    #### extract words and meanings from html files ####
    df = pd.DataFrame()
    df = extract_words_meanings_from_html_files(df, url_list_filtered)
    # export the dataframe as a csv file
    df.to_csv('Weblio_word_list.csv')

if __name__ == "__main__":
    main()