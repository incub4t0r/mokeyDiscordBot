from discord.ext import commands
import discord, datetime, os, random, json

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

global bonktracker

# Attempts to load in bonktracker.json
try:
    with open(os.path.join(file_location, 'bonktracker.json')) as f:
        bonktracker = json.load(f)
    print("Loaded bonktracker.json")
except:
    print("Could not load bonktracker.json")
    bonktracker = {}

# Creates forcible save option
def _save():    
        with open(os.path.join(file_location, 'bonktracker.json'), 'w+') as f:
            json.dump(bonktracker, f)

# Creates easy embed function
def send_msg(msg):
    emb = discord.Embed(title=None, description=msg,color=0x957530)
    return emb

# Creates class Bonktracker
class Bonktracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help = "Force the bot to save bonks",
        brief = "Force bot to save bonks"
    )
    async def save(self, ctx):
        _save()

    # Creates new bot command for bonk
    @commands.command(
        help="Send someone to horny jail",
        brief="Send someone to horny jail"
    )
    async def bonk(self, ctx, members: commands.Greedy[discord.Member]):
        bonked = ", ".join(user.name for user in members)
        resp = ""
        resp += f'{bonked} just got bonked!\n'
        for member in members:
            temp = []
            primary_id = str(member.id) 
            if primary_id not in bonktracker:
                temp.append(str(member.name))
                temp.append(0)
                bonktracker[primary_id] = temp
            bonktracker[primary_id][1] += 1
            resp += f'{str(member)[:-5]} has been bonked {str(bonktracker[primary_id][1])} time(s)\n'
        _save()
        await ctx.send(embed = send_msg(resp))

    # Creates a new bot command to list the number of bonks each user has
    @commands.command(
        help="List the number of bonks each user has",
        brief="List bonks per user"
    )
    async def test(self, ctx):
        resp = ""
        for key, value in bonktracker.items():
            resp += f'{str(value[0])} has been bonked {str(value[1])} time(s)\n'
            #print(value[0], value[1])
        await ctx.send(embed = send_msg(resp))

# https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-send-a-dm
# for future bonk dms

def setup(bot):
    bot.add_cog(Bonktracker(bot))