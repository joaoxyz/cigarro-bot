import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import choice

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

file = open("quotes.txt")
quotesList = file.readlines()
file.close()

bot = commands.Bot(command_prefix = '!')
# bot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('!cigarro')) # set custom status
    print(f'{bot.user} has connected to Discord!')

@bot.command(name = 'cigarro')
async def quote(ctx):
    await ctx.send(choice(quotesList))

bot.run(TOKEN)
