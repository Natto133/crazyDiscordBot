from dotenv import dotenv_values
import datetime
from discord.ext import commands

class StudyLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_dt = {}
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

    def get_msg(self, userid, msgid):
        if userid in self.msgs :
            if msgid in self.msgs[userid] :
                return self.msgs[userid][msgid]
        if msgid in self.msgs[0] :
            return self.msgs[0][msgid]
        return "message error"

    def should_sleep(self):
        now_time = datetime.datetime.now().time()
        bed_time = datetime.time(2)
        wakeup_time = datetime.time(3)
        if bed_time < now_time or now_time < wakeup_time:
            return True
        else:
            return False

    def show_today_result(self, userid):
        # msg = self.start_dt[userid]

        msg = self.get_msg(0, "under_development")
        return msg

    @commands.command()
    async def test(self, ctx):
        msg = f"test!{ctx.author.id}"
        await ctx.send(msg)


    @commands.command()
    async def call (self, ctx):
        print("called")
        await ctx.send(self.get_msg(ctx.author.id, "called"))

    @commands.command()
    async def ohayo(self, ctx):
        msg = ctx.author.mention
        msg += self.get_msg(ctx.author.id, "mention")
        msg += self.get_msg(ctx.author.id, "good_morning")
        await ctx.send(msg)

    @commands.command()
    async def oyasumi(self, ctx):
        result = self.show_today_result(ctx.author.id)
        msg = ctx.author.mention
        msg += self.get_msg(ctx.author.id, "mention")
        msg += self.get_msg(ctx.author.id, "good_night")
        await ctx.send(msg)

    @commands.command()
    async def start(self, ctx, arg):
        key = str(ctx.author.id) + arg
        now = self.get_dt_now()
        self.start_dt[key] = now
        msg = arg
        msg += self.get_msg(ctx.author.id, "start")
        msg += f"  [{now}]"

        if self.should_sleep():
            msg += "\n\n"
            msg += self.get_msg(ctx.author.id, "too_late")
        await ctx.send(msg)

    @commands.command()
    async def pause(self, ctx, arg):
        now = self.get_dt_now()
        msg = arg
        msg += self.get_msg(ctx.author.id, "pause")
        msg += f"  [{now}]"
        await ctx.send(msg)

    @commands.command()
    async def restart(self, ctx, arg):
        now = self.get_dt_now()
        msg = arg
        msg += self.get_msg(ctx.author.id, "restart")
        msg += f"  [{now}]"
        await ctx.send(msg)

    @commands.command()
    async def finish(self, ctx, arg):
        key = str(ctx.author.id) + arg
        now = self.get_dt_now()
        elapsed_time = datetime.datetime.strptime(now, "%Y/%m/%d %H:%M:%S") - datetime.datetime.strptime(self.start_dt[key], "%Y/%m/%d %H:%M:%S")

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
