from discord.ext import commands

class Slowmo (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slowmode(self,ctx, time: int):
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send("This command requires ``Manage Messages`` permission.")
            return
        try:
            if time == 0:
                await ctx.channel.edit(slowmode_delay=0)
                await ctx.send('Slowmode turned off.')
            elif time > 21600:
                await ctx.send("You can't set the slowmode above 6 hours.")
            else:
                await ctx.channel.edit(slowmode_delay=time)
                await ctx.send(f'Slowmode set to {time} seconds!')
        except Exception:
            await ctx.send('Oops! Something went wrong.')
