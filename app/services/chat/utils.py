from discord.message import Message
from settings import SETTINGS


def should_ignore_message(message: Message) -> bool:
    # Ignore DMs
    if message.guild is None:
        return True
    # Ignore other guilds
    if message.guild and message.guild.id != SETTINGS.DISCORD_GUILD_ID:
        return True
    # Ignore messages from the self
    if message.author == bot.user:
        return True
    # Ignore messages that don't mention the bot
    if "@Marvin" not in message.clean_content:
        return True

    return False
