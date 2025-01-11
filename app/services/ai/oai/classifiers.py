from typing import Literal, Optional

from pydantic import BaseModel
from services.ai.oai.client import client


class Intent(BaseModel):
    intent: Optional[Literal["sync-account"]]
    error: Optional[str]


def classify_intent(
    content: str,
    model: str = "gpt-4o-mini",
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
    - sync-account: The user wants to sync their account with another service.
    """

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ],
        response_format=Intent,
    )

    parsed = completion.choices[0].message.parsed

    return parsed
