from dotenv import dotenv_values
import datetime
import discord
from discord.ext import commands

class StudyLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("StudyLog init")

    def get_dt_now(self):
        now = datetime.datetime.today()
        return now.strftime("%Y/%m/%d %H:%M:%S")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test!")

    @commands.command()
    async def call (self, ctx):
        print("called")
        await ctx.send("呼び出しました [{self.get_dt_now()}]")

    @commands.command()
    async def start(self, ctx, arg):
        await ctx.send(f"{arg}を始めました！ [{self.get_dt_now()}]")

    @commands.command()
    async def pause(self, ctx, arg):
        await ctx.send(f"{arg}を中断しました！ [{self.get_dt_now()}]")

    @commands.command()
    async def restart(self, ctx, arg):
        await ctx.send(f"{arg}を再開しました！ [{self.get_dt_now()}]")

    @commands.command()
    async def finish(self, ctx, arg):
        await ctx.send(f"{arg}を終えました！ [{self.get_dt_now()}]")

async def setup(bot):
    await bot.add_cog(StudyLog(bot))
