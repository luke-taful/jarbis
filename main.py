import discord
import os
import dotenv
dotenv.load_dotenv()
token = str(os.getenv("JARBIS_TOKEN"))

jarbis = discord.Bot()

@jarbis.listen
async def on_ready():
    print(f"{jarbis.user} is online.")

@jarbis.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@jarbis.slash_command(name="kill", description="kill that guy")
async def kill(ctx: discord.ApplicationContext):
    await ctx.respond("type shit sir")

jarbis.run(token)