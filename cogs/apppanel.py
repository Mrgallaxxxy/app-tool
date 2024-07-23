import discord
from discord.ext import commands
from discord import app_commands
import asyncio 
import datetime
from Views.utils import *








class AppPannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    group = app_commands.Group(name="app", description=f"панель разработчика")
    
    @group.command(name="panel", description=f"панель разработчика")
    async def _panel(self, interaction: discord.Interaction, user: discord.Member):
        if interaction.user.id in [1196459713882243073, 744263667268321370]:
            embed = discord.Embed(
                title="Панель разработчика",
                description=f"управление участником/утилтами",
                timestamp=datetime.datetime.now()
            )
            time = discord.utils.format_dt(user.joined_at, 'R')
            embed.add_field(name="Пользователь", value=f"ID ・{user.id}\n \n Joined: {time}")
            embed.add_field(name="utils", value="・Select util from select menu・")
            await interaction.response.send_message(embed=embed, view=Utils())
        else:
            return


async def setup(bot):
    await bot.add_cog(AppPannel(bot))