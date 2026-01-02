"""
Idle Discord bot
Online only
No commands, no events
"""

import discord
import os

intents = discord.Intents.none()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Bot connected"""

client.run(os.getenv("MTQ1NjY0NTY1ODY4NDU1OTUyMQ.GaOZ-M.zRnKHfGODtGGFWSLMtZn07AT2NrZ6Mcxui_pZc"))
