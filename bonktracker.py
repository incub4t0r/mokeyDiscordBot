from discord.ext import commands
import discord, datetime, os, random, json

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

global bonktracker

try:
    with open(os.path.join(file_location, 'bonktracker.json')) as f:
        bonktracker = json.load(f)
    print("Loaded bonktracker.json")
except:
    print("Could not load bonktracker.json")
    bonktracker = {}

def _save():
        with open(os.path.join(file_location, 'bonktracker.json'), 'w+') as f:
            json.dump(bonktracker, f)

def send_msg(msg):
    emb = discord.Embed(title=None, description=msg,color=0x957530)
    return emb

class Bonktracker(commands.Cog):
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
        bonked = ", ".join(x.name for x in members)
        resp = ""
        resp += f'{bonked} just got bonked!\n'
        for member in members:
            primary_id = str(member.id)
            if primary_id not in bonktracker:
                bonktracker[primary_id] = 0
            bonktracker[primary_id] += 1
            primary_id = str(member.id)
            resp += f'{str(member)[:-5]} has been bonked {str(bonktracker[primary_id])} time(s)\n'
        _save()
        await ctx.send(embed = send_msg(resp))


# https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-send-a-dm
# for future bonk dms
def setup(bot):
    bot.add_cog(Bonktracker(bot))