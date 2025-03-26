import logfire
from openai import AsyncOpenAI
from settings import SETTINGS

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=SETTINGS.OPENAI_API_KEY,
)
logfire.configure(
    token=SETTINGS.LOGFIRE_TOKEN,
    service_name="marvin",
    environment=SETTINGS.DEPLOYENV,
)
logfire.instrument_openai(client)
