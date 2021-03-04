from discord.ext import commands
import discord, datetime, os, random, json

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

global bonktracker

# Attempts to load in bonktracker.json
try:
    with open(os.path.join(file_location, 'bonktracker.json')) as f:
        bonktracker = json.load(f)
    print("Loaded bonktracker.json for bonktracker.py")
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
            # temp = []
            primary_id = str(member.id)
            if primary_id not in bonktracker:
                # temp.append(str(member.name))
                # temp.append(0)
                bonktracker[primary_id] = 0
            bonktracker[primary_id] += 1
            resp += f'{str(member)[:-5]} has been bonked {str(bonktracker[primary_id])} time(s)\n'
        _save()
        await ctx.send(embed = send_msg(resp))

    @commands.command(
        help="List the number of bonks each user has",
        brief="List bonks per user"
    )    
    async def list_bonks(self, ctx):
        resp = ""
        resp2 = ""
        for guild in self.bot.guilds:
            async for member in guild.fetch_members(limit=None):
                if str(member.id) in list(bonktracker.keys()):
                    resp += f'{str(member).split("#")[0]} has been bonked {str(bonktracker[str(member.id)])} time(s)\n'
                else:
                    resp2 += f'{str(member).split("#")[0]} has not been bonked yet\n'
        await ctx.send(embed = send_msg(resp))
        # await ctx.send(embed = send_msg(resp2))

    # Creates a new bot command to list the number of bonks each user has
    @commands.command(
        help="List the number of bonks each user has",
        brief="List bonks per user"
    )
    async def test2(self, ctx):
        temp = sorted(bonktracker.items(), key=lambda item: item[1], reverse=True)
        resp = ""
        for key, value in temp:
            resp += f'{key} has been bonked {value} time(s)\n'
        await ctx.send(embed = send_msg(resp))
    # https://thispointer.com/sort-a-dictionary-by-value-in-python-in-descending-ascending-order/


# https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-send-a-dm
# for future bonk dms

# example of list comprehension, was originally used for list_bonks
# [print(key) for key, value in bonktracker.items()]

# example of dict keys
# print(list(bonktracker.keys()))


def setup(bot):
    bot.add_cog(Bonktracker(bot))