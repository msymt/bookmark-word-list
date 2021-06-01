# bookmark-wordbook-generator

ブックマークした[Weblio](https://ejje.weblio.jp/)のサイトから，英単語とその意味を取得し，csvファイルを出力する．

コードの大半は[こちら](https://harigami.net/cd?hsh=c4a5b7ed-8821-4d0d-a60d-e93fa69a9d65#L17)を利用させて頂きました．

君だけの単語帳を効率よく作ろう！

※Weblioには単語帳機能があるので，そちらを使う方が楽だと思います．しかし，無料枠だと200単語までしか登録できません．

## ENV

- MacOS
- Google Chrome
- Python3.5+ (maybe)

他のOSについては，`src/main.py`の`CHROME_BOOKMARK_PATH`を書き換えて下さい．

## USAGE

`src/main.py`の`folder_location_number`の値を，取得したいブックマークフォルダの番号に入れ替える．

例えば，ブックマーク内のフォルダで，英単語のフォルダが先頭(1番目, 下の`英単語集`)に設置しているなら，`0`と書く．

```
/ブックマーク
|-英単語集  # 0
|-フォルダ1 # 1
|-フォルダ2 # 2
...
```

```Python
folder_location_number = 0  # here
bookmarks = bookmark_data['roots']['bookmark_bar']['children'][folder_location_number]['children']
```

その後，以下を実行する

```bash
poetry install
poetry run python src/main.py
```

## Examples

実行するとcsv形式のファイルが出力される．以下は[novel](https://ejje.weblio.jp/content/novel)の場合

```
,0,1
0,novel ,(よい意味で)新しい、新奇な、奇抜な
```

Numbersでcsvファイルを開いた場合

![Numbers](./images/image.png)
