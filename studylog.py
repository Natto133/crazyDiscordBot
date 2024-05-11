from dotenv import dotenv_values
import datetime
import discord
from discord.ext import commands

class StudyLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("StudyLog init")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test!")

    @commands.command()
    async def call (self, ctx):
        print("called")
        await ctx.send("呼び出しました")

    @commands.command()
    async def start(self, ctx, arg):
        await ctx.send(f"{arg}を始めました！")

    @commands.command()
    async def pause(self, ctx, arg):
        await ctx.send(f"{arg}を中断しました！")

    @commands.command()
    async def restart(self, ctx, arg):
        await ctx.send(f"{arg}を再開しました！")

    @commands.command()
    async def finish(self, ctx, arg):
        await ctx.send(f"{arg}を終えました！")

async def setup(bot):
    await bot.add_cog(StudyLog(bot))
