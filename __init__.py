from redbot.core.bot import Red

from .sss import MyCog

def setup(bot: Red):
    bot.add_cog(MyCog(bot))
