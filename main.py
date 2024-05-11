import discord
from discord.ext import commands
from dotenv import dotenv_values
import studylog



config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
BOT_PREFIX = "!"
TOKEN = config["TOKEN"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

@bot.event
async def setup_hook():
    await bot.load_extension("studylog")

bot.run(TOKEN)
