from typing import Literal, Optional

from pydantic import BaseModel
from services.ai.oai.client import client
from settings import LLMConfig


class Intent(BaseModel):
    intent: Optional[
        Literal[
            "link-account",
            "unlink-account",
            "book-a-staff-meeting",
            "order-a-pizza",
            "ask-about-rules",
        ]
    ]
    error: Optional[str]


async def classify_intent(
    content: str,
) -> Intent:
    """
    Classify the intent of the user's message.
    Args:
        content (str): The message to classify.
        model (str): The model to use for classification.
    """

    SYSTEM_PROMPT = """
    Classify the intent of the user's message.
    Avaliable intents:
    - link-account: The user wants to sync their account with another service.
    - unlink-account: The user wants to remove the sync between their account and another service.
    - book-a-staff-meeting: The user wants to schedule a meeting with staff.
    - order-a-pizza: The user wants to order a pizza.
    - ask-about-rules: The user wants to ask about the rules, and regulations.
    If the user's message does not match any of these intents, return an error message.
    """

    completion = await client.beta.chat.completions.parse(
        model=LLMConfig.INTENT_CLASSIFIER_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ],
        response_format=Intent,
    )

    parsed = completion.choices[0].message.parsed

    return parsed
