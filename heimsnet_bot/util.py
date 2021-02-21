from typing import List
import discord
from discord.ext.commands import Context
from .bot import bot
import datetime
from .ping import ping


def get_owner_names() -> List[discord.User]:
    return [bot.get_user(o) for o in bot.owner_ids]


def add_owners(embed: discord.Embed):
    owners: List[discord.User] = [
        f"{u.name}#{u.discriminator}" for u in get_owner_names()
    ]
    embed.set_footer(
        text=f"Bot made by {' and '.join(owners)}",
        icon_url="https://i.ibb.co/TwtMBGh/red-bg-80x.png",
    )


def add_time(embed: discord.Embed):
    utc = arrow.utcnow()
    utc.humanize()
    embed.set_footer(text=f"Last updated at {utc}")


# -- Embeds --


def create_welcome_embed(member: discord.Member, joined: bool):
    embed = discord.Embed(
        title=
        f"Member {member.name} has {'joined' if joined else 'left'} the server!",
        description=
        f"Welcome to Heimsnet {member.name}#{member.discriminator}! Need support? Open a ticket by running `-new` in <#812858790742589490>",
        colour=discord.Colour.red(),
    )
    add_owners(embed)

    return embed


server_green = "<:servergreen:813128452147511357>"
server_red = "<:serverred:813128452718067753>"
server_yellow = "<:serveryellow:813128452260888597>"


def ping_server(id: int):
    if id == 0:
        return f"{server_green ping('server1.firenodes.com')== True else server_red}"


def create_stats_embed(ctx: Context):
    embed = discord.Embed(
        title="Heimsnet Stock",
        colour=discord.Colour.red(),
    )
    add_time(embed)

    embed.add_field("**VPS**", f"""
    {ping_server(0)}\n
    """)

    return embed
