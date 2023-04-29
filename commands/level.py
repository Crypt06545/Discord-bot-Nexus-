# import discord
# from discord import Embed, Color
# from discord.ext import commands, tasks
# from discord_components import *
# from datetime import *
# import os
# import json
# from asyncio import sleep
# import aiosqlite
# # from craiyon import Craiyon
# from io import BytesIO
# # import base64
# import random
# from easy_pil import *


# class Level(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.db = None
#         self.bot.loop.create_task(self.create_db())

#     async def create_db(self):
#         self.db = await aiosqlite.connect("level.db")
#         async with self.db.cursor() as cursor:
#             await cursor.execute(
#                 "CREATE TABLE IF NOT EXISTS levels (level INTEGER, xp INTEGER, user INTEGER, guild INTEGER)"
#             )

#     def cog_unload(self):
#         self.bot.loop.create_task(self.db.close())

#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author.bot:
#             return
#         author = message.author
#         guild = message.guild
#         async with self.db.cursor() as cursor:
#             await cursor.execute(
#                 "SELECT xp FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id)
#             )
#             xp = await cursor.fetchone()
#             await cursor.execute(
#                 "SELECT level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id)
#             )
#             level = await cursor.fetchone()

#             if not xp or not level:
#                 await cursor.execute(
#                     "INSERT INTO levels(level, xp, user, guild) VALUES (?, ?, ?, ?)", (0, 0, author.id, guild.id)
#                 )
#                 await self.db.commit()
#             try:
#                 xp = xp[0]
#                 level = level[0]
#             except TypeError:
#                 xp = 0
#                 level = 0

#             if level < 5:
#                 xp += random.randint(1, 3)
#                 await cursor.execute(
#                     "UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id)
#                 )
#             else:
#                 rand = random.randint(1, (level // 4))
#                 if rand == 1:
#                     xp += random.randint(1, 3)
#                     await cursor.execute(
#                         "UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id)
#                     )

#             if xp >= 100:
#                 level += 1
#                 await cursor.execute(
#                     "UPDATE levels SET level = ? WHERE user = ? AND guild = ?", (level, author.id, guild.id)
#                 )
#                 await cursor.execute(
#                     "UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (0, author.id, guild.id)
#                 )
#                 await message.channel.send(f"{author.mention} has leveled up to level {level}")

#             await self.db.commit()
#             await self.bot.process_commands(message)