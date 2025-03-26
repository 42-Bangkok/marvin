import asyncio
import logging

from discord import Intents
from discord.ext import commands
from discord.message import Message

# from rich import inspect # debugger
from handlers import rule_chat
from services.account.links import handle_link_account
from services.ai.oai.classifiers import classify_intent
from services.ai.oai.completions import generic_completion
from services.ai.oai.prompts import SystemPrompt
from services.chat.utils import should_ignore_message
from settings import SETTINGS, LLMConfig

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


@bot.event
async def on_message(message: Message):
    DELETE_AFTER = SETTINGS.PUBLIC_CHANNEL_MESSAGE_DELETE_AFTER
    # inspect(message) # debugger
    if should_ignore_message(message, bot.user):
        return

    async with message.channel.typing():
        intent = await classify_intent(message.clean_content)
    if intent.error:
        logging.error(intent.error)
        await message.reply(
            "Sorry, I'm not allowed to do that.",
            delete_after=DELETE_AFTER,
        )
        await message.delete(delay=DELETE_AFTER)
        return

    match intent.intent:
        case "link-account":
            link = await handle_link_account(str(message.author.id))
            tasks = [
                message.reply(
                    "I'm going to send you a DM with instructions on how to link your account.",
                    delete_after=DELETE_AFTER,
                ),
                message.author.send(
                    f"""Go to this link: {link.url} to link your account.
                        If it does not work your link code is: {link.link_code}
                        It expires at: {link.expires_at} UTC
                        """
                ),
            ]
            asyncio.gather(*tasks)

        case "order-a-pizza":
            resp = await generic_completion(
                system_prompt=SystemPrompt.MARVIN_SYSTEM_CANNOT_DO_PROMPT
                + " Tell them you can but wouldn't.",
                content=message.clean_content,
                model=LLMConfig.GENERIC_COMPLETION_MODEL,
            )
            await message.reply(
                resp,
                delete_after=DELETE_AFTER,
            )

        case "book-a-staff-meeting":
            resp = await generic_completion(
                system_prompt=SystemPrompt.MARVIN_SYSTEM_CANNOT_DO_PROMPT
                + " Also, tell them the staff is busy.",
                content=message.clean_content,
                model=LLMConfig.GENERIC_COMPLETION_MODEL,
            )
            await message.reply(
                resp,
                delete_after=DELETE_AFTER,
            )
        case "ask-about-rules":
            resp = await rule_chat.rule_chat(message.clean_content)
            await message.reply(
                resp,
                delete_after=DELETE_AFTER,
            )
        case _:
            await message.reply(
                "I cannot do that yet.",
                delete_after=DELETE_AFTER,
            )

    await message.delete(delay=DELETE_AFTER)


bot.run(SETTINGS.DISCORD_BOT_TOKEN)
