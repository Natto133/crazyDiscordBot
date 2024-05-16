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

## DB

**未実装**です。

### log.db

#### log.table

| key      | type    | describe | e.g. |
| -------- | ------- | -------- | ---- |
| id       | INTEGER | レコードID | 2 |
| userid   | INTEGER | commands.Context.author.id | 000000000000000000|
| title    | TEXT    | name of task | "赤チャ" |
| status   | INTEGER | status_id | 1 |
| datetime | TEXT    | strftime("%Y/%m/%d %H:%M:%S") | "2024/04/01 23:45:01" |

#### status.table

| status_id | category |
| --------- | -------- |
| 1      | "start"     |
| 2      | "finish"    |
| 3      | "pause"     |
| 4      | "restart"   |
| 5      | "interrupt" |

## Versions

```bash
$ python -v
Python 3.12.2

$ pip list

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
```

## .env

```.env
TOKEN = DISCORDTOKEN
ADMIN_UID = "000000000000000000"
MY_UID = "000000000000000000"
STUDY_LOG_CHANNEL_ID = "0000000000000000000"
```
