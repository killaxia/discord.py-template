from discord.ext.commands import Bot
import discord
from discord.ext import commands
intents = discord.Intents().all()
intents.reactions = True
intents.members = True







bot = Bot(command_prefix=".", intents=intents)
client = discord.Client(intents=intents)
bot.remove_command("help")
bots = []

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)


def setup(bot):
  bot.add_cog(Commands(bot))