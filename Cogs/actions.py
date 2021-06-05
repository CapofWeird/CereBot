from discord.ext import commands


class ActionCog(commands.Cog, name="Actions Cog"):

    def __init__(self, bot):
        self.bot = bot


# Setup function
def setup(bot):
    bot.add_cog(ActionCog(bot))
