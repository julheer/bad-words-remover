from os import listdir
from config import bot_token
from discord.ext import commands

client = commands.AutoShardedBot(command_prefix='!')

for filename in listdir('./src/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bot_token)
