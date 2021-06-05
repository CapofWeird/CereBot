from os import getenv

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class AdminCog(commands.Cog, name="Admin Commands"):

    def __init__(self, bot):
        self.bot = bot

    # Eval command
    @commands.command(name="eval", hidden=True)
    @commands.is_owner()
    async def eval_py(self, ctx, cmd: str):
        try:
            results = str(eval(cmd))
            await ctx.send(results)
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")

    # Prefix change function
    @commands.command(name="prefix", hidden=True)
    @commands.is_owner()
    async def change_prefix(self, ctx, prefix: str):
        try:
            self.bot.command_prefix = prefix
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS, PREFIX SET TO %s`**" % (prefix))

    # Cog loading functions
    @commands.command(name="load", hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, cog: str):
        """This command loads a cog."""
        try:
            cog = "Cogs." + cog
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**")

    @commands.command(name="unload", hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, cog: str):
        """This command unloads a cog."""
        try:
            cog = "Cogs." + cog
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**")

    @commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, cog: str):
        """This command reloads a cog."""
        try:
            cog = "Cogs." + cog
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`SUCCESS`**")

    # Bot shutdown function
    @commands.command(name="shutdown", hidden=True)
    @commands.is_owner()
    async def shutdown_bot(self, ctx):
        """This command shuts the bot down. Only the bot owner can use it."""
        try:
            await ctx.send("**`LOGGING OUT...`**")
            await self.bot.close()
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")

    # Bot reload function
    # I don"t think this command works btw
    @commands.command(name="restart", hidden=True)
    @commands.is_owner()
    async def restart_bot(self, ctx):
        """This command *should* restart the bot. But it doesn't"""
        try:
            await ctx.send("**`RESTARTING...`**")
            await self.bot.logout()
            await self.bot.login(getenv("TOKEN"))
            await ctx.send("**`SUCCESS`**")
        except Exception as e:
            await ctx.author.send(f"**`ERROR:`** {type(e).__name__} - {e}")


# Setup function
def setup(bot):
    bot.add_cog(AdminCog(bot))
