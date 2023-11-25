import asyncio
import logging

from pyrogram import Client, types, filters
from pyrogram.errors import FloodWait
from pyrogram.enums import UserStatus

from plugins.utils import get_chat_name, get_entity_id


logger = logging.getLogger(__name__)


ACTIVE_STATUSES = [UserStatus.RECENTLY, UserStatus.LAST_MONTH, UserStatus.LAST_WEEK, UserStatus.ONLINE]


@Client.on_message(filters.command("tag_active_members", prefixes=["/", "."]))
async def tag_active_members(client: Client, message: types.Message, delay: float = 1.0):
    """Example of command: /tag_active_members https://t.me/test Message to send"""

    chat_name = await get_chat_name(message=message)
    chat_id = await get_entity_id(url=chat_name, client=client)
    message_to_send = message.text.split(maxsplit=2)[-1]

    try:
        chat_members = client.get_chat_members(chat_id=chat_id)
        tag_message = " ".join(
            [f"@{member.user.username}" async for member in chat_members if member.user.status in ACTIVE_STATUSES]
        )

        tag_message_id = (await client.send_message(chat_id=chat_id, text=f"{message_to_send} {tag_message}")).id

        await asyncio.sleep(delay)

        await client.edit_message_text(chat_id=chat_id, text=message_to_send, message_id=tag_message_id)
    except FloodWait as e:
        logger.warning(f"FloodWait: {e}")
    except Exception as e:
        logger.error(f"Error: {e}")
