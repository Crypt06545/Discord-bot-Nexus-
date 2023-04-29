from discord.ext import commands
from discord import Embed, Color
import os
from dotenv import load_dotenv
import json



load_dotenv()

prefix = ">"


class Help (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")



    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = Embed(title="!Help commands", description="Use {}help <command> to extended information of a command\n**`Command Prifix: {}`**".format(
            prefix, prefix), color=Color.gold())
    

        embed.add_field(
            name="Ping :ping_pong:", value="Pings the bot and shows the response time \n> `Command: {}ping`".format(prefix), inline=True)

        embed.add_field(
            name="Who :mag_right:", value="See a member information \n> `Command: {}who`".format(prefix), inline=True)

        embed.add_field(
            name="ban :hammer:", value="Search on wikipedia \n> `Command: {}ban`".format(prefix), inline=True)


        embed.add_field(
            name="Memes", value="See meme posts\n> `Command: {}meme`".format(prefix), inline=True)

        embed.add_field(
            name="clear :wastebasket:", value="Clears the specified amount of messages\n> `Command: {}meme`".format(prefix), inline=True)

        embed.add_field(
            name="Run python code :computer:", value="Run simple python code\n> `Command: {}run`".format(prefix), inline=True)

        embed.add_field(
            name="Developer info :gear:", value="See info of Bot Developer\n> `Command: {}aboutdev`".format(prefix), inline=True)
        
        embed.add_field(
            name="weather :partly_sunny:", value="Shows the weather for the specified city\n> `Command: {}weather`".format(prefix), inline=True)
        
        embed.add_field(
            name="avatar :frame_photo:", value="Shows the avatar of the specified user or yourself\n> `Command: {}avatar`".format(prefix), inline=True)
        

        embed.add_field(
            name="calc :1234:", value="Evaluates a mathematical expression\n> `Command: {}calc`".format(prefix), inline=True)
        
        embed.add_field(
            name="level :star:", value="Shows your current level and experience points\n> `Command: {}level`".format(prefix), inline=True)
        
        embed.add_field(
            name="mute :mute:", value="Mutes the specified user\n> `Command: {}mute`".format(prefix), inline=True)
        
        embed.add_field(
            name="serverinfo :bar_chart:", value="Shows information about the server\n> `Command: {}serverinfo`".format(prefix), inline=True)
        
        embed.add_field(
            name="setprefix :pencil:", value="Changes the prefix used for commands\n> `Command: {}setprefix`".format(prefix), inline=True)
        
        embed.add_field(
            name="slowmode :turtle:", value="Sets the slowmode of the current channel\n> `Command: {}slowmode`".format(prefix), inline=True)
        
        embed.add_field(
            name="unban :hammer_pick:", value="Unbans the specified user from the server\n> `Command: {}unban`".format(prefix), inline=True)
        
        embed.add_field(
            name="unmute :loud_sound:", value="UnMutes the specified user\n> `Command: {}unmute`".format(prefix), inline=True)
        
        embed.add_field(
            name="emojify :grinning:", value="Converts your message into emojis\n> `Command: {}emojify`".format(prefix), inline=True)
        
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url_as(size=16))

        return await ctx.send(embed=embed)

    # ping command
    @help.command(name="ping")
    async def ping(self, ctx):
        embed = Embed(title="Help command",
                      description="To see the bot is online or ofline", color=Color.random())
        embed.add_field(name="Syntex", value="`{}ping`".format(prefix))
        return await ctx.send(embed=embed)
    
    # ping command
    @help.command(name="clear")
    async def clear(self, ctx):
        embed = Embed(title="Help command",
                      description="Clears the specified amount of messages", color=Color.random())
        embed.add_field(name="Syntex", value="`{}clear <number of messages(1-100)>`".format(prefix))
        return await ctx.send(embed=embed)

    # whois command
    @help.command(name="who")
    async def who(self, ctx):
        embed = Embed(title="Help command",
                      description="See a member information", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}who <mention>`".format(prefix))
        return await ctx.send(embed=embed)
    
    # whois command
    @help.command(name="avatar")
    async def avatar(self, ctx):
        embed = Embed(title="Help command",
                      description="Shows the avatar of the specified user or yourself", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}avatar <mention>`".format(prefix))
        return await ctx.send(embed=embed)



    # developer info command
    @help.command(name="aboutdev")
    async def aboutdev(self, ctx):
        embed = Embed(title="Help command",
                      description="See info of aboutdev", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}aboutdev`".format(prefix))
        return await ctx.send(embed=embed)

    # calc command
    @help.command(name="calc", aliases=["calculator"])
    async def calc(self, ctx):
        embed = Embed(title="Help command",
                      description="Calculate maths", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}calc`".format(prefix))
        return await ctx.send(embed=embed)


    # meme command
    @help.command(name="meme")
    async def meme(self, ctx):
        embed = Embed(title="Help command",
                      description="Show memes", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}meme`".format(prefix))
        return await ctx.send(embed=embed)

    # run command
    @help.command(name="run")
    async def run(self, ctx):
        embed = Embed(title="Help command",
                      description="Run python code", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}run <python code>`".format(prefix))
        return await ctx.send(embed=embed)
    # run command
    @help.command(name="weather")
    async def weather(self, ctx):
        embed = Embed(title="Help command",
                      description="Shows the weather for the specified city", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}weather <name of country or city>`".format(prefix))
        return await ctx.send(embed=embed)
   
    # run command
    @help.command(name="ban")
    async def ban(self, ctx):
        embed = Embed(title="Help command",
                      description="Bans the specified user from the server", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}ban <mention>`".format(prefix))
        return await ctx.send(embed=embed)
   
   
    # run command
    @help.command(name="unban")
    async def unban(self, ctx):
        embed = Embed(title="Help command",
                      description="Unban the specified user from the server", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}unban <mention>`".format(prefix))
        return await ctx.send(embed=embed)
   
    # run command
    @help.command(name="mute")
    async def mute(self, ctx):
        embed = Embed(title="Help command",
                      description="Mutes the specified user", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}mute <mention>`".format(prefix))
        return await ctx.send(embed=embed)
   
    # run command
    @help.command(name="unmute")
    async def unmute(self, ctx):
        embed = Embed(title="Help command",
                      description="Unmutes the specified user", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}unmute <mention>`".format(prefix))
        return await ctx.send(embed=embed)
    
    # run command
    @help.command(name="level")
    async def level(self, ctx):
        embed = Embed(title="Help command",
                      description="Shows your current level and experience points", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}level`".format(prefix))
        return await ctx.send(embed=embed)
    
    # run command
    @help.command(name="setprefix")
    async def setprefix(self, ctx):
        embed = Embed(title="Help command",
                      description="Changes the prefix used for commands", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}setprefix <your server prefix>`".format(prefix))
        return await ctx.send(embed=embed)
    
    # run command
    @help.command(name="serverinfo")
    async def serverinfo(self, ctx):
        embed = Embed(title="Help command",
                      description="Shows information about the server", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}serverinfo`".format(prefix))
        return await ctx.send(embed=embed)
    
    # run command
    @help.command(name="slowmode")
    async def slowmode(self, ctx):
        embed = Embed(title="Help command",
                      description="Sets the slowmode of the current channel", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}slowmode <number in seconds>`".format(prefix))
        return await ctx.send(embed=embed)
    
    # run command
    @help.command(name="emojify")
    async def emojify(self, ctx):
        embed = Embed(title="Help command",
                      description="Run python code", color=Color.random())
        embed.add_field(
            name="Syntex", value="`{}emojify <mention or discord image link>`".format(prefix))
        return await ctx.send(embed=embed)