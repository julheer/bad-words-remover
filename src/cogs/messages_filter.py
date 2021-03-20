from discord.ext import commands
from ..config import languages
from requests import get


class MessagesFilter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not languages:
            raise ValueError('No language(s) was selected. Please check the configuration.')

        for language in languages:
            badwords = get(
                f'https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words'
                f'/master/{language}').text.split(
                "\n")

            if message.content.lower() in badwords:
                await message.delete()

        await self.client.process_commands(message)


def setup(client):
    client.add_cog(MessagesFilter(client))
