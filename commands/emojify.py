from discord.ext import commands
from emojify import emojify_image
from typing import Union
import discord
import requests
from PIL import Image

class Emoji (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def emojify(self,ctx, url: Union[discord.Member, str], size: int = 14):
        if not isinstance(url, str):
            url = str(url.avatar_url)[:-5] + '.png'  # Updated line

        def get_emojified_image():
            r = requests.get(url, stream=True)
            image = Image.open(r.raw).convert("RGB")
            res = emojify_image(image, size)

            if size > 14:
                res = f"```{res}```"
            return res

        result = await self.bot.loop.run_in_executor(None, get_emojified_image)
        
        emoji =await ctx.reply(result)
        await emoji.add_reaction("🤬")
        await emoji.add_reaction("🤣")
        await emoji.add_reaction("🥺")
