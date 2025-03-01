from pydantic import validate_call
from services.ai.oai.client import client


@validate_call
async def generic_completion(
    system_prompt: str,
    content: str,
    max_tokens: int = 512,
    model: str = "google/gemini-2.0-flash-lite-001",
) -> str:
    """
    Classify the intent of the user's message.
    Args:
        content (str): The message to classify.
        model (str): The model to use for classification.
    """

    completion = await client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ],
        max_tokens=max_tokens,
    )

    content = completion.choices[0].message.content

    return content
