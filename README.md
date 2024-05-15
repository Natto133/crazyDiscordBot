# 俺の使用人Bot

## ToDo

- [ ] 記録の保存を二重配列化  
- [ ] 記録のバックアップ(ファイル)  
- [ ] DBに保存  
- [x] oha/oyasu機能(今日の記録のリセット、Result表示)
- [x] ohayoメッセージ機能
- [x] should_sleepの実装(寝る時間が近いときのメッセージ返答)
- [ ] slash commands にする
- [x] 型のアノテーションつける(つけられるっぽい）

## Versions

Python 3.12.2

Package       Version
------------- -------
aiohttp       3.9.5
aiosignal     1.3.1
attrs         23.2.0
discord.py    2.3.2
frozenlist    1.4.1
idna          3.7
multidict     6.0.5
pip           24.0
python-dotenv 1.0.1
yarl          1.9.4

## .env

```.env
TOKEN = DISCORDTOKEN
ADMIN_UID = "000000000000000000"
MY_UID = "000000000000000000"
STUDY_LOG_CHANNEL_ID = "0000000000000000000"
```
