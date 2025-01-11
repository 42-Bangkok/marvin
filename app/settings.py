from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DISCORD_GUILD_ID: int
    DISCORD_BOT_TOKEN: str
    FE_URL: str


SETTINGS = Settings()
