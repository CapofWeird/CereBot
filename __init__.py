import os
from sys import stderr
from traceback import print_exc

from discord import Game, __version__
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

activity = Game("Cerebos: The Crystal City")
path = os.getcwd()

bot = Bot(
    command_prefix='-',
    description="A bot to help run Cerebos on Discord!",
    owner_id=457637280539082763,
)

if __name__ == "__main__":
    print("Loading bot cogs...\n")
    with os.scandir(path + r"\Cogs") as dir:
        for cog in dir:
            if cog.name[-3:] == ".py":  # We only want files with .py extension
                try:
                    bot.load_extension(f"Cogs.{cog.name}".strip(".py"))
                    print(f"SUCCESS - Loaded cog: {cog.name}")
                except Exception as e:
                    print(f"\nERROR - Failed to load extension: {cog.name}.\n",
                          file=stderr)
                    print_exc()
                    print("\n")


@bot.event
async def on_ready():
    await bot.change_presence(activity=activity)
    print(f"\nLogged in as {bot.user.name} - {bot.user.id}")
    print(f"Discord.py version: {__version__}")
    print("Successfully logged in and booted!\n")

bot.run(os.getenv("TOKEN"))
