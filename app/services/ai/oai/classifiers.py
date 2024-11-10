from typing import Literal, Optional
from pydantic import BaseModel
from services.ai.oai.client import client


class Intent(BaseModel):
    intent: Optional[Literal["sync-account"]]


def classify_intent(content: str) -> Intent:
    """
    Classify the intent of the user's message.
    """

    PROMPT = """
    Given the following message, classify the intent of the user's message.
    sync-account: The user wants to sync their account with another service.
    If the intent is not clear, return None.
    """
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": content},
        ],
        response_format=Intent,
    )

    parsed = completion.choices[0].message.parsed

    return parsed
