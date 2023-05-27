#invite link ('https://discord.com/api/oauth2/authorize?client_id=1108691489267138601&permissions=8&scope=bot')


import io
import discord
from discord.ext import commands
import aiohttp
import json
import asyncio
from datetime import datetime, timedelta

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.guilds = True # Ajout de l'intention guilds

client = commands.Bot(command_prefix='<', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}!')

@client.command()
async def online_members(ctx):
    """Affiche les informations des membres en ligne dans un embed."""
    online_members = []
    for member in ctx.guild.members:
        if member.status == discord.Status.online:
            online_members.append(member)

    embed = discord.Embed(title="Membres en ligne", color=discord.Color.green())

    for member in online_members:
        activities = member.activities
        if activities:
            activity = activities[0]
            if isinstance(activity, discord.CustomActivity):
                activity_name = activity.name
            else:
                activity_name = activity.type.name.capitalize()
        else:
            activity_name = "Aucune activité"

        joined_at = member.joined_at.strftime("%d/%m/%Y %H:%M:%S")

        embed.add_field(name=f"Membre: {member.name}", value=f"Activité: {activity_name}\nRejoint le: {joined_at}", inline=False)

    await ctx.send(embed=embed)


client.run("MTEwODY5MTQ4OTI2NzEzODYwMQ.GA0kL2.p28dTu5T60S8wlUpOj0lVcH4P-Q17FBnUtbjWI")