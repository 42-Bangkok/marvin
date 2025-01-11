import nanoid
from pydantic import BaseModel
from settings import SETTINGS


class LinkAccountResponse(BaseModel):
    token: str
    url: str


async def handle_link_account(
    discord_user_id: int,
) -> LinkAccountResponse:
    """
    Handle the linking of an account.
    Args:
        discord_user_id (int): The Discord user ID to link.
    """
    token = nanoid.generate()
    # TODO: Save the token to the database along with the Discord user ID
    return LinkAccountResponse(
        token=token, url=f"{SETTINGS.FE_URL}/accounts/link/?token={token}"
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
