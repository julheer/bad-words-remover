import config
from requests import get
from discord.ext import commands

client = commands.AutoShardedBot(command_prefix="!")

@client.event
async def on_ready():
	print(f"Started as {client.user}.")


@client.event
async def on_message(message):
	for language in config.languages:
		badwords = get(f"https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/{language}").text.split("\n")
		
		if message.content.lower() in badwords:
			await message.delete()
			# You can also add your own actions after deleting messages.

	await client.process_commands(message)


client.run(config.bot_token)
