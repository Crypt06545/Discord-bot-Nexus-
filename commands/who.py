from discord.ext import commands
import discord
from datetime import datetime
class Who (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def who(self,ctx, member:discord.Member):
        roles = [role for role in member.roles]

        embed = discord.Embed(title=f"Name: {member.name}",
                        desription=member.mention, color=discord.Color.random(), timestamp=datetime.utcnow())

        embed.add_field(name="ID: ", value=member.id, inline=True)
        embed.add_field(
            name="Status", value=f"`{member.status}`", inline=True)
        embed.add_field(name="Activity",
                        value=f"`{member.activity}`", inline=False)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Roles:", value="".join(
            [role.mention for role in roles]), inline=False)

        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                            text=f"Request by {ctx.author.name}")
        return await ctx.reply(embed=embed)