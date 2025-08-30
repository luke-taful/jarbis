import discord
import os
import dotenv
dotenv.load_dotenv()
token = str(os.getenv("JARBIS_TOKEN"))

jarbis = discord.Bot()

@bot.event
async def on_ready():
    print(f"{jarbis.user} is online.")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

jarbis.run(token)