from typing import List
import discord
from .bot import bot


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


def create_welcome_embed(member: discord.Member, joined: bool):
    embed = discord.Embed(
        title=f"Member {member.name} has {'joined' if joined else 'left'} the server!",
        description=f"Welcome to Heimsnet {member.name}#{member.discriminator}! Need support? Open a ticket by running `-new` in <#812858790742589490>",
        colour=discord.Colour.red(),
    )
    add_owners(embed)

    return embed
