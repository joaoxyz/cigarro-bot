import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # do something with message
    print(message.content)

    if message.content == 'cigarro':
        await message.channel.send('Quer ganhar um caminhão de CIGARRO? Envie CIGARRO para (21) 8837-4423 para concorrer a um caminhão de CIGARRO!')

bot.run(TOKEN)
