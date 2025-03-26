from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application.
    Environment variables:
    DEPLOYENV: Deployment environment (local or prod)
    OPENAI_API_KEY: OpenAI API key
    DISCORD_GUILD_ID: Discord guild ID
    DISCORD_BOT_TOKEN: Discord bot token
    FE_URL: Frontend URL
    SERVICE_TOKEN: Service token for authentication
    PUBLIC_CHANNEL_MESSAGE_DELETE_AFTER: Time in seconds to delete messages in public channels
    LOGFIRE_TOKEN: Logfire token for logging
    """

    DEPLOYENV: Literal["local", "prod"]
    OPENAI_API_KEY: str
    DISCORD_GUILD_ID: int
    DISCORD_BOT_TOKEN: str
    FE_URL: str
    SERVICE_TOKEN: str
    PUBLIC_CHANNEL_MESSAGE_DELETE_AFTER: int = 15
    LOGFIRE_TOKEN: str


class LLMConfig:
    GENERIC_COMPLETION_MODEL = "google/gemini-2.0-flash-lite-001"
    INTENT_CLASSIFIER_MODEL = "openai/gpt-4o-mini"
    RULE_CHAT_MODEL = "google/gemini-2.0-flash-001"


SETTINGS = Settings()
