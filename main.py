import discord
from discord.ext import commands
from decouple import config
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot("/", intents=intents)

@bot.event
async def on_ready():
  await bot.tree.sync()
  print("Bot inicializado com sucesso!")

@bot.command()
async def ola(ctx:commands.Context):
  await ctx.reply(f"Olá {ctx.author.mention}, tudo bem?")

@bot.command()
async def hora(ctx:commands.Context):  
  hora_atual = datetime.now().strftime("%H:%M:%S")
  await ctx.reply(f"Olá {ctx.author.mention}, a hora atual é {hora_atual}")

bot.run(config("TOKEN"))