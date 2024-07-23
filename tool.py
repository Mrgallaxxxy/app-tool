
token = str(input("Enter token: "))





from discord.ext import commands, tasks
import discord
import logging
import os
import asyncio

# Настройка логирования
дщп = logging.basicConfig(level=logging.DEBUG)


bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())


@bot.event
async def on_connect():
    await bot.tree.sync()


@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)}ms")




async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f'[+] {filename} loaded')



async def main():
    discord.utils.setup_logging()
    await load()
    await bot.start(token=token, reconnect=True)



if __name__ == "__main__":
    asyncio.run(main())