from discord.ext import commands

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx):
        guild = ctx.guild
        user = ctx.author

        target_channel = None
        for vc in guild.voice_channels:
            for m in vc.members:
                if m == user:
                    target_channel = vc

        if target_channel:
            for m in target_channel.members:
                await m.edit(mute=True)

        await ctx.message.delete()

    @commands.command()
    async def unmute(self, ctx):
        guild = ctx.guild
        user = ctx.author

        target_channel = None
        for vc in guild.voice_channels:
            for m in vc.members:
                if m == user:
                    target_channel = vc

        if target_channel:
            for m in target_channel.members:
                await m.edit(mute=False)

        await ctx.message.delete()


def setup(bot):
    bot.add_cog(MuteCog(bot))