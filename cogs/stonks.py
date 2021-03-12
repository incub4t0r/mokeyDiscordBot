from discord.ext import commands
import discord, datetime, os, random, json
import yfinance as yf

file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

global stonks

def send_msg(msg):
        emb = discord.Embed(title=None, description=msg,color=0x957530)
        return emb

class Stonks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        help = "list bitcoin prices",
        brief = "list BTC ticker"
    )
    async def bitcoin(self, ctx):
        resp = ""
        bitcoin = yf.Ticker("BTC-USD")
        price = bitcoin.info["regularMarketPrice"]
        resp += f"BTC is at ${str(price)}"
        await ctx.send(embed = send_msg(resp))
        
def setup(bot):
    bot.add_cog(Stonks(bot))