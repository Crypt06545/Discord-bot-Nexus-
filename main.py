import discord
from discord import Embed, Color
from discord.ext import commands, tasks
from discord_components import *
from datetime import *
import os
import json
from asyncio import sleep
import aiosqlite
# from craiyon import Craiyon
from io import BytesIO
# import base64
import random
from easy_pil import *

from itertools import cycle
from dotenv import load_dotenv

from server import keep_alive

from commands.help import Help
from commands.meme import Meme
from commands.emojify import Emoji
from commands.ping import Ping
from commands.serverinfo import ServerInfo
from commands.weather import Weather
from commands.who import Who
from commands.about_dev import AboutDEV
from commands.slowmo import Slowmo
from commands.clear import Clear
from commands.avatar import Avatar
from commands.pai_run import Runpy
from commands.calculator import Calculator
from commands.ban import Ban
from commands.unban import UnBan


load_dotenv()


status = cycle(['dm me monkey💻'])
@tasks.loop()
async def status_swap():
    await client.change_presence(activity=discord.Game(next(status)))


now = datetime.utcnow()
def get_prefix(client, message):

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

intents = discord.Intents().all()
client = commands.Bot(command_prefix= get_prefix, intents=intents)
client.remove_command("help")
DiscordComponents(client)



@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    status_swap.start()
    setattr(client, "db", await aiosqlite.connect("level.db"))
    async with client.db.cursor() as cursor:
        await cursor.execute("CREATE TABLE IF NOT EXISTS levels (level INTEGER, xp INTEGER, user INTEGER, guild INTEGER)")
        # await cursor.execute("CREATE TABLE IF NOT EXISTS levelsSettings(levelsys BOOL, role INTEGER, levelrq INTEGER, guild INTEGER)")



@client.event
async def on_message(message):
    if message.author.bot:
        return
    author = message.author
    guild = message.guild
    async with client.db.cursor() as cursor:
        # await cursor.execute("SELECT levelsys FROM levelsSettings WHERE guild = ?",())

        await cursor.execute('SELECT xp FROM levels WHERE user = ? AND guild = ?', (author.id, guild.id,))
        xp = await cursor.fetchone()
        await cursor.execute('SELECT level FROM levels WHERE user = ? AND guild = ?', (author.id, guild.id,))
        level = await cursor.fetchone()

        if not xp or not level:
            await cursor.execute('INSERT INTO levels(level, xp, user, guild) VALUES (?, ?, ?, ?)', (0, 0, author.id, guild.id,))
            await client.db.commit()
        try:
            xp = xp[0]
            level = level[0]
        except TypeError:
            xp = 0
            level = 0
        
        
        
        if level < 5:
            xp += random.randint(1, 3)
            await cursor.execute('UPDATE levels SET xp = ? WHERE user = ? AND guild = ?', (xp, author.id, guild.id,))
        else:
            rand = random.randint(1, (level//4))
            if rand == 1:
                xp += random.randint(1, 3)
                await cursor.execute('UPDATE levels SET xp = ? WHERE user = ? AND guild = ?', (xp, author.id, guild.id,))


        if xp >= 100:
            level += 1
            # print(level)
            # print(xp)
            await cursor.execute('UPDATE levels SET level = ? WHERE user = ? AND guild = ?', (level, author.id, guild.id,))
            await cursor.execute('UPDATE levels SET xp = ? WHERE user = ? AND guild = ?', (0, author.id, guild.id,))
            await message.channel.send(f"{author.mention} has leveled up to level {level}")

    await client.db.commit()
    await client.process_commands(message)
 


@client.command()
async def level(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    async with client.db.cursor() as cursor:
        await cursor.execute('SELECT xp FROM levels WHERE user = ? AND guild = ?', (member.id, ctx.guild.id,))
        xp = await cursor.fetchone()
        await cursor.execute('SELECT level FROM levels WHERE user = ? AND guild = ?', (member.id, ctx.guild.id,))
        level = await cursor.fetchone()

        if not xp or not level:
            await cursor.execute('INSERT INTO levels(level, xp, user, guild) VALUES (?, ?, ?, ?)', (0, 0, member.id, ctx.guild.id,))
            
        try:
            xp = xp[0]
            level = level[0]
        except TypeError:
            xp = 0
            level = 0
        
    user_data = {
        "xp": xp,
        "name": f"{member.name}#{member.discriminator}",
        "level": level,
        "next_level_xp": 100,
        "percentage": xp,
    }

    background = Editor(Canvas((900, 300), color="#1c1c1c"))
    profile_picture = await load_image_async(str(member.avatar_url))
    profile = Editor(profile_picture).resize((150, 150)).circle_image()

    poppins = Font.poppins(size=40)
    poppins_small = Font.poppins(size=30)

    card_right_shape = [(600, 0), (750, 300), (900, 300), (900, 0)]

    background.polygon(card_right_shape, color="#2c2c2c")
    background.paste(profile, (30, 30))

    background.rectangle((30, 220), width=650, height=40, color="#2c2c2c", radius=20,)
    background.bar((30, 220), max_width=650, height=40, percentage=user_data["percentage"], color="#7289da", radius=20,)
    background.text((200, 40), user_data["name"], font=poppins, color="#FFFFFF")

    background.rectangle((200, 100), width=350, height=2, fill="#FFFFFF")
    background.text(
        (200, 130),
        f"Level - {user_data['level']} | XP - {user_data['xp']}/{user_data['next_level_xp']}",
        font = poppins_small,
        color= "#FFFFFF",
    )

    file = discord.File(fp=background.image_bytes, filename="levelcard.png")
    await ctx.reply(file=file)



@client.event
async def on_member_join(member):
    # print(member.guild.id)
    with open("channel.json") as f:
        channel = json.load(f)        
        channelID = channel[str(member.guild.id)]

    welcomeEmbed = discord.Embed(title=f"Welcome To The Server!!! ", description=f"{member.mention} has joined the server 🎉🎉", color=discord.Color.blue())
    welcomeEmbed.set_thumbnail(url=member.avatar_url)
    await client.get_channel(int(channelID)).send(embed=welcomeEmbed) #here need to paste the varriable



@client.event
async def on_member_remove(member):
    with open("channel.json") as f:
        channel = json.load(f)        
        channelID = channel[str(member.guild.id)]
    farewellEmbed = discord.Embed(title=f"Has Left the server :(", description=f"{member.mention} চলে গেস তাতে কি নতুন একটা পেয়ে যাব।😎", color=discord.Color.red())
    farewellEmbed.set_thumbnail(url=member.avatar_url)
    await client.get_channel(int(channelID)).send(embed=farewellEmbed)


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        prefixes[str(guild.id)] = '>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def setprefix(ctx, prefixset = None):
    if (not ctx.author.guild_permissions.manage_channels):
        await ctx.send("This command needs ``Manage Channels`` permission")
        return
    if (prefixset == None):
        prefixset = '>'

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefixset

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'The bot prefix has been changed to {prefixset}')


    
@client.command()
async def kick(ctx,member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send("This command need ``kick permission``")
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')
                                     

@client.command()
async def mute(ctx,member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send("This command need ``Manage permission``")
        return
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name ="Muted")

    if not muteRole:
        await ctx.send("The Muted role has not been found!!")
        return        

    await member.add_roles(muteRole, reason=reason)
    await ctx.send("User is Muted")
    await member.send(f'You have been Muted from **{guild.name}** | Reason: **{reason}**')

                                     
@client.command()
async def unmute(ctx,member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send("This command need ``Mute permission``")
        return
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name ="Muted")

    if not muteRole:
        await ctx.send("The Muted role has not been found..")

    await member.remove_roles(muteRole, reason=reason)
    await ctx.send("User is Unmuted")
    await member.send(f'You have been Unmuted from **{guild.name}** | Reason: **{reason}**')







# @client.command()
# async def gnerate(ctx: commands.context, *, prompt: str):
#     ETA = int(time.time() + 60)
#     msg = await ctx.send(f'Grap A Cup of Coffee.. ETA: <t:{ETA}:R>')
#     generator = Craiyon()
#     result = generator.generate(prompt)
#     images = result.images
#     for i in images:
#         image_bytes = base64.decodebytes(i.encode("utf-8"))
#         image_file = discord.File(BytesIO(image_bytes), filename="image.png")
#         await ctx.send(file=image_file)





# @client.command()
# async def board(ctx):
#     async with client.db.cursor as cursor:
#         await cursor.execute("SELECT levelsys FROM levelSettings WHERE guid = ?", (ctx.guild.id,))
#         levelsys = await cursor.fetchone()
#         if levelsys:
#             if not levelsys[0] == 1:
#                 return await ctx.send("LEVEL system is disabled by this server!")
#         await cursor.execute("SELECT level, xp, user FROM levels WHERE guid = ? ORDER BY xp DESC, xp DESC LIMIT 10", (ctx.guild.id,))
#         data = await cursor.fetchall()
#         if data:
#             em = discord.Embed(title="Leveling LeaderBoard")
#             count = 0
#             for table in data:
#                 count +=1
#                 user = ctx.guild.get_member(table[2])
#                 em.add_field(name=f'{count}. {user.name}', value=f'Level-**{table[0]}** | xp-**{table[1]}**', inline=False)

#             return await ctx.send(embed=em)
#         return await ctx.reply("There are no User stored in LeaderBoard ._.")


@client.command()
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.errors.CommandNotFound):
        embed = discord.Embed(title="Invalid command",
                              description="That command is not recognized",
                              color=discord.Color.red())
        msg = await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(
            title="Missing argument",
            description="One or more required arguments are missing",
            color=discord.Color.red())
        msg = await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="❌Error",
                              description=str(error),
                              color=discord.Color.red())
        msg = await ctx.send(embed=embed)



    await sleep(5)
    await msg.delete()

client.add_cog(Help(client))
client.add_cog(Meme(client))
client.add_cog(Emoji(client))
client.add_cog(Ping(client))
client.add_cog(ServerInfo(client))
client.add_cog(Weather(client))
client.add_cog(Who(client))
client.add_cog(AboutDEV(client))
client.add_cog(Slowmo(client))
client.add_cog(Clear(client))
client.add_cog(Avatar(client))
client.add_cog(Runpy(client))
client.add_cog(Calculator(client))
client.add_cog(Ban(client))
client.add_cog(UnBan(client))

keep_alive()
   
client.run(os.getenv("DISCORD_TOKEN"))
