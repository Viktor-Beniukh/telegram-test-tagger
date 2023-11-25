import logging
import configparser

from pyrogram import Client

from logging_conf.logging_config import setup_logging


setup_logging()


logger = logging.getLogger(__name__)


config = configparser.ConfigParser()
config.read("config.ini")
plugins = dict(root="plugins")

app = Client(
    "account",
    api_id=int(config["pyrogram"]["api_id"]),
    api_hash=config["pyrogram"]["api_hash"],
    plugins=plugins
)


if __name__ == "__main__":
    app.run()
