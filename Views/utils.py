from discord.ext import commands
from discord.ui import *
import discord



class Utils(View):
    def __init__(self):
        super().__init__(timeout=None)
    @select(
        placeholder="Select util",
        options=[
            discord.SelectOption(label="channel util", value="1", description=f"управление каналами"),
            discord.SelectOption(label="role util", value="2", description=f"уравление ролями"),
            discord.SelectOption(label="server util", value="3", description=f"уравление сервером")
        ]
    )
    async def select(self, interaction: discord.Interaction, select: Select):
        if interaction.user.id in [1196459713882243073, 744263667268321370]:
            if select.values[0] == "1":
                pass
            else:
                pass
        else:
            pass