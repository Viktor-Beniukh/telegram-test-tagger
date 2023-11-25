import asyncio
import logging
from datetime import datetime
from pytz import UTC

from pyrogram import Client, types, filters
from pyrogram.errors import FloodWait

from plugins.utils import get_chat_name, get_entity_id


logger = logging.getLogger(__name__)


@Client.on_message(filters.command("tag_by_date", prefixes=["/", "."]))
async def tag_by_date(client: Client, message: types.Message, delay: float = 1.0):
    """
    Example of command: /tag_by_date https://t.me/test 30 20.09.2023 Message to send
    third argument - limit messages
    fourth argument - date in format 20.09.2023 (d.m.y)
    """

    chat_name = await get_chat_name(message=message)
    chat_id = await get_entity_id(url=chat_name, client=client)
    limit_messages = int(message.text.split()[2])
    last_activity_date = datetime.strptime(message.text.split()[3], "%d.%m.%Y").replace(tzinfo=UTC)
    message_to_send = message.text.split(maxsplit=4)[-1]
    message_from_history = client.get_chat_history(chat_id=chat_id, limit=limit_messages)

    tag_message = ""
    usernames_date = []
    async for message_history in message_from_history:
        message_date = message_history.date.replace(tzinfo=UTC)
        if last_activity_date == message_date:
            if message_history.from_user.username not in usernames_date:
                usernames_date.append(message_history.from_user.username)
    for username_date in usernames_date:
        tag_message += f"@{username_date} "

    try:
        tag_message_id = (await client.send_message(chat_id=chat_id, text=f"{message_to_send} {tag_message}")).id

        await asyncio.sleep(delay)

        await client.edit_message_text(chat_id=chat_id, text=message_to_send, message_id=tag_message_id)
    except FloodWait as e:
        logger.warning(f"FloodWait: {e}")
    except Exception as e:
        logger.error(f"Error: {e}")
