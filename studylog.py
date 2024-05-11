from dotenv import dotenv_values
import datetime
import discord
from discord.ext import commands

class StudyLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_dt = {}
        print("StudyLog init")

    def get_dt_now(self):
        now = datetime.datetime.today()
        return now.strftime("%Y/%m/%d %H:%M:%S")

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f"test!{ctx.author.id}")

    @commands.command()
    async def call (self, ctx):
        print("called")
        await ctx.send("呼び出しました [{self.get_dt_now()}]")

    @commands.command()
    async def start(self, ctx, arg):
        key = str(ctx.author.id) + arg
        now = self.get_dt_now()
        self.start_dt[key] = now
        msg = f"{arg}を始めました！ [{now}]"
        await ctx.send(msg)

    @commands.command()
    async def pause(self, ctx, arg):
        await ctx.send(f"{arg}を中断しました！ [{self.get_dt_now()}]")

    @commands.command()
    async def restart(self, ctx, arg):
        await ctx.send(f"{arg}を再開しました！ [{self.get_dt_now()}]")

    @commands.command()
    async def finish(self, ctx, arg):
        key = str(ctx.author.id) + arg
        now = self.get_dt_now()
        elapsed_time = datetime.datetime.strptime(now, "%Y/%m/%d %H:%M:%S") - datetime.datetime.strptime(self.start_dt[key], "%Y/%m/%d %H:%M:%S")

        msg = f"{arg}を終えました！ [{now}]"
        msg += f"\n時間：{elapsed_time}"
        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(StudyLog(bot))
