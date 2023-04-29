from discord.ext import commands

class Clear (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def clear(self,ctx, amount = 11):
        if (not ctx.author.guild_permissions.manage_messages):
            await ctx.send("This command need ``manage permission``")
            return
        amount = amount+1
        if amount > 101:
            await ctx.send("can Not delete more than 100 message")

        else:
            await ctx.channel.purge(limit = amount)
            await ctx.send("cleared message")