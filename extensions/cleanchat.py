import hikari
import lightbulb
from lightbulb import commands

cleanchat_pl = lightbulb.plugins.Plugin(
    name="CleanChat",
    description=None
)

cc_channel_ids = []
cc_whitelist = []

@cleanchat_pl.listener(hikari.GuildMessageCreateEvent)
async def remove_message(event):
    if not event.is_human or event.content in cc_whitelist:
        return
    elif (event.channel_id in cc_channel_ids):
        await cleanchat_pl.bot.rest.delete_message(event.channel_id, event.message)
    

@cleanchat_pl.command
@lightbulb.command('cleanchat', 'Clean chat settings')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def cleanchat(ctx):
    pass


@cleanchat.child
@lightbulb.command('set', 'Start or stop removing messages on this channel.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cleanchat_set(ctx):
    if (ctx.channel_id in cc_channel_ids):
        cc_channel_ids.remove(ctx.channel_id)
        await ctx.respond('This channel will no longer be cleaned.')
    else:
        cc_channel_ids.append(ctx.channel_id)
        await ctx.respond('This channel will be cleaned from now on.')

@cleanchat.child
@lightbulb.option('word', 'Word that you want to whitelist.', required=False)
@lightbulb.command('whitelist', 'Whitelist words to not remove.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cleanchat_whitelist(ctx):
    if(ctx.options.word == None):
        await ctx.respond('Whitelisted words: `{}`'.format(cc_whitelist))
        pass
    else:
        if(ctx.options.word in cc_whitelist):
            cc_whitelist.remove(ctx.options.word)
            await ctx.respond('`{}` has been removed from the whitelist.'.format(ctx.options.word))
        else:
            cc_whitelist.append(ctx.options.word)
            await ctx.respond('`{}` has been added to the whitelist.'.format(ctx.options.word))

        
def load(bot) -> None:
    bot.add_plugin(cleanchat_pl)

def unload(bot) -> None:
    bot.remove_plugin(cleanchat_pl)