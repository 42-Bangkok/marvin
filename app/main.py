import asyncio
import logging

from discord import Intents
from discord.ext import commands
from discord.message import Message
from rich import inspect
from services.account.links import handle_link_account
from services.ai.oai.classifiers import classify_intent
from settings import SETTINGS

intents = Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")


def _should_ignore_message(message: Message) -> bool:
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


@bot.event
async def on_message(message: Message):
    inspect(message)
    if _should_ignore_message(message):
        return

    async with message.channel.typing():
        intent = await classify_intent(message.clean_content)

    if intent.error:
        logging.error(intent.error)
        await message.reply("Sorry, I'm not allowed to do that.")
        return

    if intent.intent == "link-account":
        link = await handle_link_account(message.author.id)
        tasks = [
            message.reply(
                "I'm going to send you a DM with instructions on how to link your account."
            ),
            message.author.send(f"1. proceed to this link: {link.url}"),
        ]
        asyncio.gather(*tasks)


bot.run(SETTINGS.DISCORD_BOT_TOKEN)
