# Telegram tagger

Telegram tagger of members in the chatroom written on python using pyrogram


### Installing using GitHub

- Python3 must be already installed

```shell
git clone https://github.com/Viktor-Beniukh/telegram-test-tagger.git
cd telegram-test-tagger
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

```
You can create `.env` file and add there the variables with your according values(optionally)
(see the sample in the file `.env.sample`):
- `CHAT_URL`: this is chat address of your telegram channel;

You need to create `config.ini` file and add there the variables with your according values 
(see the sample in the file `config.sample.ini`):
- `api_id` and `api_hash`: parameters required for user authorization 
                           to develop your own application using the Telegram API 
                           (`https://core.telegram.org/api/obtaining_api_id`);
- proxy data(optionally);
- plugins.



## Features

- Ability to tag all chat participants;
- Ability to mark chat participants by activity;
- Ability to adjust marks by date;
- Ability to mark by keywords;
- Logging of the most critical parts of the project code.
