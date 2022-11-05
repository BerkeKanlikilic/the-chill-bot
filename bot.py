import os

import hikari
import lightbulb

bot = lightbulb.BotApp(
    token=os.environ["DISCORD_TOKEN"],
    default_enabled_guilds=(595372655981494388)
)

@bot.command
@lightbulb.command('ping', 'Responds with pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f"Pong! {bot.heartbeat_latency * 1_000:.0f}ms")

bot.load_extensions_from('./extensions')
bot.run(
    asyncio_debug=True
)