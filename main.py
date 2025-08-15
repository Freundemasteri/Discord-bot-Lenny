import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Hier deinen Token einsetzen
bot.run("MTQwNjAyMzkyNTkyNTkzNzI3Mg.GH9rH-.YsLHWTMxc5XUjN0rBT-Lx-yDEmX4KlpxWXSyu0")
