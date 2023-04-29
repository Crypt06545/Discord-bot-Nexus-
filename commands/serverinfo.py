from discord.ext import commands
import discord
import requests

class ServerInfo (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self,ctx):
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        serverinfoEmbed = discord.Embed(title=f"Server Information for {ctx.guild.name}", color=ctx.author.color, timestamp=ctx.message.created_at)
        serverinfoEmbed.set_thumbnail(url=ctx.guild.icon_url)
        serverinfoEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        serverinfoEmbed.add_field(name="Admin", value= f'{ctx.guild.owner.name}')
        serverinfoEmbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}', inline=True)
        serverinfoEmbed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=True)
        serverinfoEmbed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=True)
        serverinfoEmbed.add_field(name='\u200b', value='\u200b', inline=False)
        serverinfoEmbed.add_field(name='Number of Roles', value=str(role_count), inline=True)
        serverinfoEmbed.add_field(name='\u200b', value='\u200b', inline=True)
        serverinfoEmbed.add_field(name='Bots', value=', '.join(list_of_bots), inline=True)
        serverinfoEmbed.set_footer(text=f"Server created at {ctx.guild.created_at.strftime('%Y-%m-%d %H:%M:%S')} UTC", icon_url=self.bot.user.avatar_url)
        await ctx.send(f"{ctx.author.mention}", embed=serverinfoEmbed)
