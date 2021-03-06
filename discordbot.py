import os
from discord.ext import commands

INITIAL_EXTENSIONS = [
    'cogs.pingpongcog',
    'cogs.mutecog'
]

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')


if __name__ == '__main__':
    if os.getenv('TOKEN'):
        bot = MyBot(command_prefix='!')
        bot.run(os.getenv('TOKEN'))
    else:
        print('plz env "TOKEN"')