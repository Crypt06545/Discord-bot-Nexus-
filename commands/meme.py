from discord.ext import commands
import discord
import requests

class Meme (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self,ctx):
        response = requests.get("https://meme-api.com/gimme").json()
        title = response['title']
        image_url = response['url']
        author = response['author']
        subreddit = response['subreddit']
        embed = discord.Embed(title=title, color=discord.Color.blue())
        embed.set_image(url=image_url)
    
        m = await ctx.send(embed=embed)
        await m.add_reaction("😂")
        await m.add_reaction("👍")
        await m.add_reaction("👎")
