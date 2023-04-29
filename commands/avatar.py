from discord.ext import commands
import discord

class Avatar (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def avatar(self,ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        memberAvatar = member.avatar_url
        avaEmbed = discord.Embed(title = f"{member.name}'s Avatar")
        avaEmbed.set_image(url= memberAvatar)
        await ctx.reply(embed = avaEmbed)
                                