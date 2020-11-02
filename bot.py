import os
import discord
import asyncio
from dotenv import load_dotenv
from random import choice

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

quotesList = [
             'Quer ganhar um caminhão de CIGARRO? Envie CIGARRO para (21) 8837-4423 para concorrer a um caminhão de CIGARRO!',
             'A estética do cigarro é daora pena q da cancer',
             'Ô gente boa\nÔ gente boa\nEi\nTem cigarro aí?\nCigarro\nTem cigarro aí?',
             'Pois eu gosto muito de cigarro e vô fuma bastante cigarro hmmm hmmm cigarro hmmm',
             'Quem puder me ceder um cigarro neste momento difícil eu agradeço',
             'MUSICAS PARA FUMAR CIGARRO',
             'o cigarro une as pessoas',
             'hoje não almocei estou a base de pão água e cigarro qualquer hora eu morro',
             'filho da puta, deu dois socao na minha cabeça só pq acendi um cigarro dentro do quarto pnc',
             'MINHA MÃE MEXEU NAS MINHAS COISAS E ENCONTROU CIGARRO',
             'Vontade de comprar cigarro',
             'Quer um cigarro amigo?',
             'me segurando p n ir comprar cigarro pq n posso fumar mais'
]
bot = commands.Bot(command_prefix = 'cig.')
# bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='frase')
async def quote(ctx):
    await ctx.send(choice(quotesList))

bot.run(TOKEN)
