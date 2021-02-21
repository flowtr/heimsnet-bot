import discord
from discord.channel import TextChannel
from discord.ext import commands
from .util import create_welcome_embed
from .bot import bot
from .config import config


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(
        name="Heimsnet tickets", type=discord.ActivityType.watching))


@bot.command(name="hello")
async def hello(message: discord.Message):
    await message.channel.send("Hello world!")


@bot.event
async def on_member_join(member: discord.Member):
    if config["welcome_channel"].exists():
        ch: TextChannel = bot.get_channel(config["welcome_channel"].get(int))
        # True = joined the server
        await ch.send(embed=create_welcome_embed(member, True))


@bot.event
async def on_member_remove(member: discord.Member):
    if config["welcome_channel"].exists():
        ch: TextChannel = bot.get_channel(config["welcome_channel"].get(int))
        # False = left the server
        await ch.send(embed=create_welcome_embed(member, False))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.NotOwner):
        await ctx.send("You must be a bot owner to run this command!")
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("That command wasn't found! Sorry :(")


def main():
    bot.load_extension("jishaku")
    bot.run(config["token"].get(str))
