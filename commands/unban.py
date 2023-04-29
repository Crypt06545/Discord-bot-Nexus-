from discord.ext import commands


class UnBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    async def unban(self, ctx, *, member):
        if (not ctx.author.guild_permissions.ban_members):
            await ctx.send("This command needs `ban permission`")
            return

        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

        # If the member is not found in the banned list, send a message indicating that
        await ctx.send(f'Member "{member}" not found in the ban list.')
