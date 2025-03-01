from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DISCORD_GUILD_ID: int
    DISCORD_BOT_TOKEN: str
    FE_URL: str
    SERVICE_TOKEN: str


class LLMConfig:
    GENERIC_COMPLETION_MODEL = "google/gemini-2.0-flash-lite-001"
    INTENT_CLASSIFIER_MODEL = "openai/gpt-4o-mini"
    RULE_CHAT_MODEL = "google/gemini-2.0-flash-001"


SETTINGS = Settings()
