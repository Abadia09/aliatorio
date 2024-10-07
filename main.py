import discord 
import os
import random
from discord.ext import commands

 
intents = discord.Intents.default()
intents.message_content = True

 
bot = commands.Bot(command_prefix='$', intents=intents)
 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

 

@bot.command()
async def caricaturas(ctx):
    lista_imagenes = os.listdir('imagenes caricaturas')
    imagen_seleccionada = random.choice(lista_imagenes)
    with open(f'imagenes caricaturas/{imagen_seleccionada}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

 
bot.run("")
