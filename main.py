from http import client
import os
import random
import crazyDiscordBot_token
import discord
#from discord.ext import commands

BOT_PREFIX = ("?", "!")
TOKEN = crazyDiscordBot_token.token
client = discord.Client()
#client = commands.Bot(command_prefix=BOT_PREFIX)

# リプライ時の返答(実行テスト)
async def reply(message):
    reply = f'{message.author.mention}なんだい？ぼくを呼ぶなんて珍しいじゃないか。\nでも、忘れないで。ぼくは一生きみの友だちだよ！(v0.1.4)'
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

client.run(TOKEN)