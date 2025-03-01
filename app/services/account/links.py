from datetime import datetime

import httpx
from pydantic import BaseModel, validate_call
from settings import SETTINGS


class LinkAccountResponse(BaseModel):
    link_code: str
    expires_at: datetime
    url: str


@validate_call
async def handle_link_account(
    discord_id: str,
) -> LinkAccountResponse:
    """
    Handle the linking of an account.
    Args:
        discord_user_id (int): The Discord user ID to link.
    """
    client = httpx.AsyncClient(base_url=f"{SETTINGS.FE_URL}/api")
    r = await client.post(
        "/link/discord/generate-link-code",
        headers={"Authorization": f"Bearer {SETTINGS.SERVICE_TOKEN}"},
        json={"discord_id": discord_id},
    )
    r.raise_for_status()
    data = r.json()
    return LinkAccountResponse(
        link_code=data["link_code"],
        expires_at=data["expires_at"],
        url=f"{SETTINGS.FE_URL}/link/discord/?token={data["link_code"]}",
    )


async def handle_unlink_account(
    discord_user_id: int,
) -> None:
    """
    Handle the unlinking of an account.
    Args:
        discord_user_id (int): The Discord user ID to unlink.
    """
    return True
