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
    reply = f'{message.author.mention}なんだい？ぼくを呼ぶなんて珍しいじゃないか。\nでも、忘れないで。ぼくは一生きみの友だちだよ！'
    await message.channel.send(reply)

@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)

client.run(TOKEN)