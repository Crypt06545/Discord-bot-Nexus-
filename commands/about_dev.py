from discord.ext import commands
import discord


class AboutDEV (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def aboutdev(self,ctx):
        embed = discord.Embed(
            title="About the Developer",
            description="Here's some information about the developer of this bot!",
            color=0x3498db
        )

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Name", value="***MEHADI HASAN***, ***ROFSON JAME***", inline=False)
        embed.add_field(name="GitHub", value="[github.com/Crypt06545](https://github.com/Crypt06545)", inline=False)
        embed.add_field(name="Discord", value="```Crypt0◥▶_◀◤#4680``` & ```rofson17#0467```", inline=False)
        embed.add_field(name="Website", value="[mehadi.com](https://mehadi.onrender.com)", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url_as(size=16))

        await ctx.send(embed=embed)

