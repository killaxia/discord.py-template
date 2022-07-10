from discord.ext.commands import Bot
import discord
from discord.ext import tasks
intents = discord.Intents().all()
intents.reactions = True
intents.members = True
import os.path
import requests



bot = Bot(command_prefix="-", intents=intents)
token = 'OTk0MDU5NjU5MDI5NzkwNzIx.G-qRS0.eFdXvFK6KwHLCcdPJycUBb2RXUMN8W1vAbB_N0'
client = discord.Client(intents=intents)
bot.remove_command("help")
botid = []



for filename in os.listdir('/var/bots/template/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"{filename} loaded!")


@bot.event
async def on_ready():
    print('Member count updated')
    print("Bot in server: {}".format("Success"))
    print("Bot name: {}".format(bot.user.name))
    ip = requests.get('https://ipinfo.io/ip').text
    print(ip)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f'{members} members'))
    f = open("/var/bots/members.txt", "a")
    f.write(str(members)+"\n")
    f.close()

  

#run token
bot.run(token)