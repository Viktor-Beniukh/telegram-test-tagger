import logging

from pyrogram import Client, types
from pyrogram.errors import ChatIdInvalid


logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


async def get_entity_id(client: Client, url: str) -> int:

    try:
        chat_info = await client.get_chat(url)
        return chat_info.id
    except ChatIdInvalid:
        logger.error(f"Invalid chat URL: {url}")
    except Exception as e:
        logger.error(f"Error: {e}")


async def get_chat_name(message: types.Message) -> str:
    return message.text.split()[1].split("/")[-1]
