from services.ai.oai.completions import generic_completion
from services.ai.oai.prompts import SystemPrompt
from settings import LLMConfig


async def rule_chat(
    content: str,
) -> str:
    with open("docs/ft_bkk_rules.md", mode="rb") as f:
        rules = f.read().decode("utf-8")
    system_prompt = SystemPrompt.RULE_CHAT + "\n" + rules
    completion = await generic_completion(
        system_prompt=system_prompt,
        content=content,
        max_tokens=100_000,
        model=LLMConfig.RULE_CHAT_MODEL,
    )
    return completion
