from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[LOG] Application successfully started. Logged as {self.client.user}.')


def setup(client):
    client.add_cog(Listeners(client))
