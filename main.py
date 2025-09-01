import discord
import os
import dotenv
import requests
dotenv.load_dotenv()
token = str(os.getenv("JARBIS_TOKEN"))

def serverStatus():
    url = "https://www.edsm.net/api-status-v1/elite-server"
    response = requests.get(url)
    response = response.json()
    return(response)

jarbis = discord.Bot()

@jarbis.listen
async def on_ready():
    print(f"{jarbis.user} is online.")

@jarbis.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@jarbis.slash_command(name="servers", description="galnet news update")
async def news(ctx: discord.ApplicationContext):
    servers = serverStatus()
    await ctx.respond(f"Servers are {servers["message"]} as of {servers["lastUpdate"]}")


jarbis.run(token)