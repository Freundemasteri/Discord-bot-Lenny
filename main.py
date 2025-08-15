import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # nötig für Ban, Kick, Timeout

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')

# Kick-Command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} wurde gekickt. Grund: {reason}")

# Ban-Command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} wurde gebannt. Grund: {reason}")

# Timeout-Command (Dauer in Sekunden)
@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, duration: int, *, reason=None):
    try:
        await member.timeout_for(duration, reason=reason)
        await ctx.send(f"{member.mention} wurde für {duration} Sekunden gemutet. Grund: {reason}")
    except Exception as e:
        await ctx.send(f"Fehler: {e}")

# Bot starten (Token einfügen)
bot.run("MTQwNjAyMzkyNTkyNTkzNzI3Mg.GH9rH-.YsLHWTMxc5XUjN0rBT-Lx-yDEmX4KlpxWXSyu0")
