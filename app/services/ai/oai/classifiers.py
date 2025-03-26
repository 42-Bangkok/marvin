from typing import Literal, Optional

from pydantic import BaseModel
from services.ai.oai.client import client
from services.ai.oai.prompts import SystemPrompt
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
    model: str | None = None,
) -> Intent:
    """
    Classify the intent of the user's message.
    Args:
        content (str): The message to classify.
        model (Optional[str]): The model to use for classification. If None, defaults to LLMConfig.INTENT_CLASSIFIER_MODEL.
    """

    completion = await client.beta.chat.completions.parse(
        model=model if model else LLMConfig.INTENT_CLASSIFIER_MODEL,
        messages=[
            {"role": "system", "content": SystemPrompt.INTENT_CLASSIFIER},
            {"role": "user", "content": content},
        ],
        response_format=Intent,
    )

    parsed = completion.choices[0].message.parsed

    return parsed
