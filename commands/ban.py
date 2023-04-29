from discord.ext import commands
import discord

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if not ctx.author.guild_permissions.ban_members:
            await ctx.send("This command requires ``ban permission``")
            return
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned")