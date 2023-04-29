
from discord.ext import commands
import io
import contextlib
class Runpy (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def run_py(self,ctx, *, code):
        if "import" in code or "while True:" in code:
            return await ctx.send("Please run simple code, don't import aynthing or while True anything")
        str_obj = io.StringIO()
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            return await ctx.send(f"```{e.__class__.__name__}: {e}```")
        await ctx.send(f'```{str_obj.getvalue()}```')
