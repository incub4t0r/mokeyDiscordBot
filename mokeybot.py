import discord, os
from discord.ext import commands
from dotenv import load_dotenv
# Unused imports: datetime, random, json, asyncio

# Gets mokeybot.py file location for future reference
#file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Loads .env variables (not uploaded to github for obvious reasons)
load_dotenv()

# Grabs TOKEN and GUILD from .env 
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Creates new command prefix for calling the bot
bot = commands.Bot(command_prefix="!")

# Creates easy embed function
def send_msg(msg):
    emb = discord.Embed(title=None, description=msg,color=0x957530)
    return emb

# Logs in bot
@bot.event
async def on_ready():
    print('Logged in')
    print(f"Username: {bot.user.name}")
    print('-----')
    # Unused command to change status on discord
    # await bot.change_presence(activity=discord.Game(name=""))

# Creates new bot command for bonk
@bot.command(
    help="Send someone to horny jail",
    brief="Send someone to horny jail"
)
async def bonk(ctx, members: commands.Greedy[discord.Member]):
    bonked = ", ".join(x.name for x in members)
    resp = f'{bonked} just got bonked!'
    await ctx.send(embed = send_msg(resp))

# Shows source for bot
@bot.command(
    help="Provides the github source for the bot",
    brief="See the code"
)
async def source(ctx):
    resp = 'https://github.com/incub4t0r/mokeyDiscordBot'
    await ctx.send(embed = send_msg(resp))

bot.run(TOKEN)

# TODO
# add bonk tracker