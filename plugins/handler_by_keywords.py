import asyncio
import logging

from pyrogram import Client, types, filters
from pyrogram.errors import FloodWait

from plugins.utils import get_chat_name, get_entity_id


logger = logging.getLogger(__name__)


KEY_WORDS: set[str] = {"keyword1", "keyword2", "keyword3"}


@Client.on_message(filters.command("tag_by_keywords", prefixes=["/", "."]))
async def tag_by_keywords(client: Client, message: types.Message, delay: float = 1.0) -> None:
    """
    Example of command: /tag_by_keywords https://t.me/test 30 Message to send
    third argument - limit messages
    """

    chat_name = await get_chat_name(message=message)
    chat_id = await get_entity_id(url=chat_name, client=client)
    limit_messages = int(message.text.split()[2])
    message_to_send = message.text.split(maxsplit=3)[-1]
    message_from_history = client.get_chat_history(chat_id=chat_id, limit=limit_messages)

    tag_message = ""
    usernames_keywords = []
    async for message_history in message_from_history:
        for keyword in KEY_WORDS:
            if keyword.lower() in message_history.text.lower():
                if message_history.from_user.username not in usernames_keywords:
                    usernames_keywords.append(message_history.from_user.username)
    for username_keywords in usernames_keywords:
        tag_message += f"@{username_keywords} "

    try:
        tag_message_id = (await client.send_message(chat_id=chat_id, text=f"{message_to_send} {tag_message}")).id

        await asyncio.sleep(delay)

        await client.edit_message_text(chat_id=chat_id, text=message_to_send, message_id=tag_message_id)
    except FloodWait as e:
        logger.warning(f"FloodWait: {e}")
    except Exception as e:
        logger.error(f"Error: {e}")
