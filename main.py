import discord
import os
import dotenv
import requests
import json
dotenv.load_dotenv()
token = str(os.getenv("JARBIS_TOKEN"))
tenorToken = str(os.getenv("TENOR_TOKEN"))

def serverStatus():
    url = "https://www.edsm.net/api-status-v1/elite-server"
    response = requests.get(url)
    response = response.json()
    return(response)

def tenorSearch(search_term):
    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s&media_filter=%s&random=%s" % (search_term, tenorToken, "jarbis_discord_bot", 1, "tinygif", True))
    if r.status_code == 200:
        gifs = json.loads(r.content)
        print(gifs)
        gif = gifs["results"][0]["media_formats"]["tinygif"]["url"]

        return gif
    else:
        return None

jarbis = discord.Bot()

@jarbis.listen
async def on_ready():
    print(f"{jarbis.user} is online.")

@jarbis.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@jarbis.slash_command(name="servers", description="elite server status")
async def serverCheck(ctx: discord.ApplicationContext):
    servers = serverStatus()
    await ctx.respond(f"Servers are {servers["message"]} as of {servers["lastUpdate"]}")

@jarbis.slash_command(name="true", description="get this man a true")
async def getThisManATrue(ctx: discord.ApplicationContext):
    gif = tenorSearch("morgan freeman true")
    # print(gif)
    await ctx.respond(gif)
    # if gif:
    #     await ctx.respond(gif)
    # else:
    #     await ctx.respond(f"No True :(")

jarbis.run(token)