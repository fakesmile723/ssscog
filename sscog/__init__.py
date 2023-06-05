from redbot.core.bot import Red

from .sss import MyCog

async def setup(bot: Red):
   await bot.add_cog(MyCog(bot))
