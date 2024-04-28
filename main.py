from http import client
import os
import random
import discord
from discord.ext import commands
import crazyDiscordBot_token
import studylog

BOT_PREFIX = ("?", "!")
TOKEN = crazyDiscordBot_token.token
client = discord.Client()
bot = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
        await client.get_channel(1084423841343885392).send("我起床せり") 

@client.event
async def reply(message):
    reply = f'{message.author.mention}なんだい？ぼくを呼ぶなんて珍しいじゃないか。\nでも、忘れないで。ぼくは一生きみの友だちだよ！(v0.1.4 @{message.channel.id})'
    await message.channel.send(reply)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        await reply(message)

    if message.content == "ワロタ" or message.content == "わろた":
        await message.channel.send(f"{message.author.mention}\n＿人人人人人人人人人人人人人人人人人人人人＿\n＞　ワロタンゴタンバリンシャンシャン半島　＜\n￣Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣")

    if message.content == "w" or message.content == "ｗ" or message.content == "くさ" or message.content == "草":
        await message.channel.send("地球温暖化対策に貢献できて偉い！\nでも草を生やすな")

@bot.event
async def setup_hook():
    await bot.load_extension("studylog")

client.run(TOKEN)
