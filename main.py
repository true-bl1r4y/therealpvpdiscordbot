import discord

Botname = "therealpvp"
state = ""
isbotonline = True

if isbotonline:
    state = True

intents = discord.Intents.none()
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    Botname, state
    print(f"{Botname} is online: {state}")

token = "MTQ1NjY0NTY1ODY4NDU1OTUyMQ.G78qNp.6Aj-5nBJHve601aq8cqa5NDG5E6wu6ycFEtvjs"
client.run(token)
