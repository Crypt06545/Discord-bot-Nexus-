from discord.ext import commands
import discord
from discord_components import Button, ButtonStyle
from datetime import datetime, timedelta

class Calculator(commands.Cog):
    buttons = [
        [
            Button(style=ButtonStyle.grey, label="1"),
            Button(style=ButtonStyle.grey, label="2"),
            Button(style=ButtonStyle.grey, label="3"),
            Button(style=ButtonStyle.blue, label="×"),
            Button(style=ButtonStyle.red, label="Exit"),
        ],
        [
            Button(style=ButtonStyle.grey, label="4"),
            Button(style=ButtonStyle.grey, label="5"),
            Button(style=ButtonStyle.grey, label="6"),
            Button(style=ButtonStyle.blue, label="÷"),
            Button(style=ButtonStyle.red, label="⌫"),
        ],
        [
            Button(style=ButtonStyle.grey, label="7"),
            Button(style=ButtonStyle.grey, label="8"),
            Button(style=ButtonStyle.grey, label="9"),
            Button(style=ButtonStyle.blue, label="+"),
            Button(style=ButtonStyle.red, label="Clear"),
        ],
        [
            Button(style=ButtonStyle.grey, label="00"),
            Button(style=ButtonStyle.grey, label="0"),
            Button(style=ButtonStyle.grey, label="."),
            Button(style=ButtonStyle.blue, label="-"),
            Button(style=ButtonStyle.green, label="="),
        ],
    ]

    def __init__(self, client):
        self.client = client

    def calculator(self, exp):
        o = exp.replace('×', '*')
        o = o.replace('÷', '/')
        result = ''
        try:
            result = str(eval(o))
        except:
            result = 'An error occurred'
        return result

    @commands.command()
    async def calc(self, ctx):
        m = await ctx.send(content='Loading Calculator')
        expression = 'None'
        delta = datetime.utcnow() + timedelta(minutes=5)
        e = discord.Embed(title=f'{ctx.author.name}\'s | {ctx.author.id}', description=expression, timestamp=delta)
        await m.edit(components=self.buttons, embed=e)

        while m.created_at < delta:
            res = await self.client.wait_for('button_click')
            if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[0].timestamp < delta:
                expression = res.message.embeds[0].description
                if expression == 'None' or expression == 'An error occurred':
                    expression = ''
                if res.component.label == "Exit":
                    await res.respond(content='calculator closed', type=7)
                    break
                elif res.component.label == '⌫':
                    expression = expression[:-1]
                elif res.component.label == 'Clear':
                    expression = None
                elif res.component.label == '=':
                    expression = self.calculator(expression)
                else:
                    expression += res.component.label

                f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression, timestamp=delta)
                await res.respond(content="", embed=f, components=self.buttons, type=7)


