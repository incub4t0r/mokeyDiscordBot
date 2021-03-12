import discord, os, random, json
from discord.ext import commands
from dotenv import load_dotenv
# Unused imports: datetime, asyncio


### SETUP ###
# Gets mokeybot.py file location for future reference
file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Loads .env variables (not uploaded to github for obvious reasons)
load_dotenv()

# Grabs TOKEN and GUILD from .env 
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('GUILD_ID')

# Creates new command prefix for calling the bot, enables intents as well
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Creates easy embed function
def send_msg(msg):
    emb = discord.Embed(title=None, description=msg,color=0x957530)
    return emb


# Attempts to load modules

modules = ["bonktracker", "stonks"]

for cog in modules:
    try:
        bot.load_extension(f'cogs.{cog}')
        print(f'Loaded {cog}.py')
    except:
        print(f'Error loading {cog}')


### COMMANDS ###
# Logs in bot
@bot.event
async def on_ready():
    print('Logged in')
    print(f"Username: {bot.user.name}")
    print('-----')
    # Command to change status on discord
    await bot.change_presence(activity=discord.Game(name="hugging pogchamps"))

# Shows source for bot
@bot.command(
    help="Provides the github source for the bot",
    brief="See the code"
)
async def source(ctx):
    resp = 'Written by incub4t0r/43y3s\nhttps://github.com/incub4t0r/mokeyDiscordBot'
    await ctx.send(embed = send_msg(resp))

# Ping pong
@bot.command(
    help = "Utilizes 1337 coding to determine correct response and latency",
    brief = "Prints pong and latency"
)
async def ping(ctx):
    resp = f'Pong! {bot.latency}'
    await ctx.send(embed = send_msg(resp))

# Prints message back, simon says
@bot.command(
    help = "Parses using a for loop an entire message and returns it",
    brief = "Prints your message back"
)
async def echo(ctx, *args):
    resp = ""
    for arg in args:
        resp = resp + " " + arg
    await ctx.send(embed = send_msg(resp))

# Leftover command definition from testing for list_bonks
@bot.command(
    help="test"
)
async def test(ctx):
    resp = ""
    # guild = bot.get_guild(GUILD_ID)
    # print(guild.members)
    # for member in guild.members:
    #     print (member)
    async for member in ctx.guild.fetch_members(limit=None):
        print("{},{}".format(member,member.id))
    await ctx.send(embed = send_msg(resp))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = send_msg("No such command, use !help to view commands"))
    else:
        raise error


bot.run(TOKEN)

### TODO
# add bonk tracker --- DONE

### NOTES

# [print(cogname) for cogname in modules]

# one line example for loading multiplle cogs
# [bot.load_extension(f'cogs.{cogname}') for cogname in modules]

# async def list_bonks(ctx):
#     resp = ""
#     guild = bot.get_guild(GUILD_ID)
#     async for member in ctx.guild.fetch_memebers(limit=None):
#         resp += f'{str(member)[:5]} has been bonked {str(bonktracker[member.id])} time(s)\n'
#     # for key, value in bonktracker.items():
#     #     resp += f'{str(value[0])} has been bonked {str(value[1])} time(s)\n'
#     #     #print(value[0], value[1])
#     await ctx.send(embed = send_msg(resp))
# Catches command errors
