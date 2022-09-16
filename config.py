## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuxYi4hb5egrKE_2iKrS2GOI4easlxcbP5eNj_2JtrVwR-3kd6xlRZb6jHk0vOq-lnV_o7lrAeR1b9tqYU7k5pa7uLvOClXThWHP0ldYwUFckml8wfH3-WpKzkZWOnQWMtGpOfJNx8Wdz-qCVw48Xl7Vup4Rw5Ux8K543gGo4ZzrQT7nY9akIyPrXFFioPPWS9K2t6z6yYlzA-gj-TFgqr1VREmQgPXrK3PTuQueziWogSKVCDInNaK7Z7IJZKx6IwrIjyPKZfwG2byDafZ8PG2LUSsojakFgSWatmfrv7WfDmLbefMgpf3RO2Chp1wUrd3YrSneI_AyGzbWAXjq5scs=")
BOT_TOKEN = getenv("BOT_TOKEN", "5449841253:AAHBwOmHcXg_dlo9d3SzuA1cgQvwdx4wO8g")
BOT_NAME = getenv("BOT_NAME", "𝙈𝙪𝙨𝙞𝙘 𝙎𝙥𝙞𝙙𝙚𝙧")
API_ID = int(getenv("API_ID", "11888980"))
API_HASH = getenv("API_HASH", "a041669ed71104ef5a6e00234b3bd2f6")
OWNER_NAME = getenv("OWNER_NAME", "كـسـول")
OWNER_USERNAME = getenv("OWNER_USERNAME", "O_Q_M")
ALIVE_NAME = getenv("ALIVE_NAME", "Lourdmahdi")
BOT_USERNAME = getenv("BOT_USERNAME", "Music_Spider_BBot")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Music_Spiderr")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "soeoos")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "u_n_n_n")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1862918421").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
