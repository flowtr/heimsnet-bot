from discord import message
import discord
from discord.ext import commands
from .config import config

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix=config["prefix"].get(str),
    owner_ids=[int(o) for o in config["owners"].get(str).split(",")],
    intents=intents,
)
