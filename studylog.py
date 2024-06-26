from typing import List, Dict, Final
from dotenv import dotenv_values
import datetime
import sqlite3
import discord
from discord.ext import commands

class StudyLog(commands.Cog):

    STATUS_ID: Final[List[str]] = ["reset", "start", "finish", "pause", "restart", "interrupt"]

    def __init__(self, bot):
        self.bot = bot

        self.start_dt: Dict[str, str] = {} # {title: start date time"%Y/%m/%d %H:%M:%S"}
        self.total_time: Dict[int, datetime.timedelta] = {}   # {00000(uid): datetime.time,}

        con = sqlite3.connect("./log.db")
        con.execute("""
            CREATE TABLE IF NOT EXISTS log(
                id INTEGER PRIMARY KEY,
                userid INTEGER,
                title TEXT,
                status_id INTEGER,
                datetime TEXT
            )""")
        con.close()

        self.msgs = {
                0: {
                    "under_development": "（この機能は開発中です。）",
                    "called": "呼び出しました。",
                    "mention": "君、",
                    "good_morning": "おはようございます！",
                    "good_night": "今日も一日お疲れ様でした。\n良い夢を！",
                    "todays_result": "【本日の成果】",
                    "start": "を開始しました！",
                    "pause": "を一時停止しました！",
                    "restart": "を再開しました！ ",
                    "finish": "を終えました！",
                    "too_late": "もう夜遅いですしお体に障りますから、これを最後にされてはいかがですか？",
                }
            }

        print("StudyLog init")


    def get_dt_now(self):
        now = datetime.datetime.today()
        return now.strftime("%Y/%m/%d %H:%M:%S")


    def insert_log(self, userid: int, title: str, status_id: int, datetime: str):
        con = sqlite3.connect("./log.db")
        con.execute("""INSERT INTO log
                (userid, title, status_id, datetime) VALUES(?, ?, ?, ?)""",
                (userid, title, status_id, datetime)
            )
        con.commit()
        con.close()


    # def select_log(self, ):
    #     con = sqlite3.connect("file:log.db?mode=ro", uri=True)
    #     res = con.execute("SELECT * FROM log")
    #     res.fetchall()
    #     con.close()


    def get_msg(self, userid:int, msgid:str):
        # 登録済み
        if userid in self.msgs :
            if msgid in self.msgs[userid] :
                return self.msgs[userid][msgid]
            else :
                return self.msgs[0][msgid]
        # 未登録
        else :
            if msgid in self.msgs[0] :
                return self.msgs[0][msgid]

        return "message error"


    def should_sleep(self):
        now_time = datetime.datetime.now().time()
        bed_time = datetime.time(22)
        wakeup_time = datetime.time(3)
        # if bed_time < now_time or now_time < wakeup_time:
        #     return True
        # else:
        #     return False
        return bed_time < now_time or now_time < wakeup_time


    def show_today_result(self, userid:int):
        con = sqlite3.connect("file:log.db?mode=ro", uri=True)
        res = con.execute("SELECT * FROM log WHERE userid=?", (str(userid),))
        logs: List = res.fetchall()
        con.close()

        # datetimeをstrからdatetime.datetimeに変換
        for i in range(len(logs)):
            logs[i][4] = datetime.datetime.strptime(logs[i][4], "%Y/%m/%d %H:%M:%S")

        # ToDo: logsの処理

        if userid in self.total_time :
            msg = str(self.total_time[userid])
        else :
            msg = "0"

        return msg


    # ===以下、command===

    @commands.command()
    async def test(self, ctx: commands.Context):
        msg = f"test!{ctx.author.id}"
        await ctx.send(msg)


    @commands.command()
    async def call (self, ctx: commands.Context):
        print("called")
        await ctx.send(self.get_msg(ctx.author.id, "called"))


    @commands.command()
    async def ohayo(self, ctx: commands.Context):
        self.total_time.pop(ctx.author.id)
        self.total_time.setdefault(ctx.author.id, datetime.timedelta())

        msg = ctx.author.mention
        msg += self.get_msg(ctx.author.id, "mention")
        msg += self.get_msg(ctx.author.id, "good_morning")
        await ctx.send(msg)


    @commands.command()
    async def oyasumi(self, ctx: commands.Context):
        result = self.show_today_result(ctx.author.id)

        msg = ctx.author.mention
        msg += self.get_msg(ctx.author.id, "mention")
        msg += self.get_msg(ctx.author.id, "good_night")
        msg += "\n\n"
        msg += self.get_msg(ctx.author.id, "todays_result")
        msg += result
        await ctx.send(msg)


    @commands.command()
    async def start(self, ctx: commands.Context, arg: str):
        key = str(ctx.author.id) + arg
        now = self.get_dt_now()
        self.start_dt[key] = now

        self.insert_log(ctx.author.id, arg, 1, now)

        msg = arg
        msg += self.get_msg(ctx.author.id, "start")
        msg += f"  [{now}]"

        if self.should_sleep():
            msg += "\n\n"
            msg += self.get_msg(ctx.author.id, "too_late")
        await ctx.send(msg)


    @commands.command()
    async def pause(self, ctx: commands.Context, arg: str):
        now = self.get_dt_now()

        self.insert_log(ctx.author.id, arg, 3, now)

        msg = arg
        msg += self.get_msg(ctx.author.id, "pause")
        msg += f"  [{now}]"
        await ctx.send(msg)


    @commands.command()
    async def restart(self, ctx: commands.Context, arg :str):
        now = self.get_dt_now()

        self.insert_log(ctx.author.id, arg, 4, now)

        msg = arg
        msg += self.get_msg(ctx.author.id, "restart")
        msg += f"  [{now}]"
        await ctx.send(msg)


    @commands.command()
    async def finish(self, ctx: commands.Context, arg: str):
        key = str(ctx.author.id) + arg
        now = self.get_dt_now()
        elapsed_time = datetime.datetime.strptime(now, "%Y/%m/%d %H:%M:%S") - datetime.datetime.strptime(self.start_dt[key], "%Y/%m/%d %H:%M:%S")
        self.total_time.setdefault(ctx.author.id, datetime.timedelta())
        self.total_time[ctx.author.id] += elapsed_time

        self.insert_log(ctx.author.id, arg, 2, now)

        msg = arg
        msg += self.get_msg(ctx.author.id, "finish")
        msg += f"  [{now}]"
        msg += f"\n時間：{elapsed_time}"

        if self.should_sleep():
            msg += "\n\n"
            msg += self.get_msg(ctx.author.id, "too_late")

        await ctx.send(msg)


async def setup(bot):
    await bot.add_cog(StudyLog(bot))
