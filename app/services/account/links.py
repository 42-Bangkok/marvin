from datetime import datetime

import httpx
import nanoid
from pydantic import BaseModel
from settings import SETTINGS


class LinkAccountResponse(BaseModel):
    link_code: str
    expires_at: datetime
    url: str


async def handle_link_account(
    discord_id: int,
) -> LinkAccountResponse:
    """
    Handle the linking of an account.
    Args:
        discord_user_id (int): The Discord user ID to link.
    """
    token = nanoid.generate()
    client = httpx.AsyncClient(base_url=f"{SETTINGS.FE_URL}/api")
    r = await client.post(
        "/link/discord/generate-link-code",
        json={"discord_id": discord_id},
    )
    r.raise_for_status()
    data = r.json()
    return LinkAccountResponse(
        link_code=data["link_code"],
        expires_at=data["expires_at"],
        url=f"{SETTINGS.FE_URL}/accounts/link/?token={token}",
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
