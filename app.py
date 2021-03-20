import config
from requests import get
from discord.ext import commands

client = commands.AutoShardedBot(command_prefix="!")

for filename in os.listdir('./src/cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


client.run(config.bot_token)
