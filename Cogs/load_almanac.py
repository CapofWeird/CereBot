import json
import os
from random import choice, randint

from discord.ext import commands

# from data.defs.game import Event


class LoadAlmanac(commands.cog, name="Load Almanac"):

    def __init__(self, bot):
        self.bot = bot

    filepath = "Data\\Events"

    all_events = []

    for file in os.scandir(filepath):
        with open(file.path) as entry:
            all_events.append(json.load(entry))

    foo = choice(all_events)
    category = list(foo)[0]
    bar = foo.get(category)


def setup(bot):
    bot.add_cog(LoadAlmanac(bot))
