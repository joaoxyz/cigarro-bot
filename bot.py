import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import choice
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

file = open('quotes.txt', encoding='utf-8')
quotesList = file.readlines()
file.close()

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('!cigarro')) # set custom status
    print(f'{bot.user} has connected to Discord!')

@bot.command(name = 'cigarro')
async def quote(ctx):
    await ctx.send(choice(quotesList))

keep_alive()
bot.run(TOKEN)
