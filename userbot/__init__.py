from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from logging import basicConfig, getLogger, INFO
from telethon.tl.functions.channels import JoinChannelRequest
#from core.database import Environment
import time, glob
from dotenv import load_dotenv
import os
from core.functions import time_formatter, update_init


load_dotenv("config.env")
basicConfig(format="%(asctime)s - @TomrisUserBot - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
UPSTREAM_URL = "https://tomrisuserbot.org/modules"
DB_URI = "sqlite:///tomrisdb.db"
if STRING_SESSION:
  bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
  bot = TelegramClient("tomris", API_KEY, API_HASH)

with bot:
  try:
    bot(JoinChannelRequest("@TomrisUserBot"))
    bot(JoinChannelRequest("@TomrisSupport"))
  except:
    pass
  me = bot.get_me()
  uid = me.id
#  update_init(UPSTREAM_URL)
VERSION = "V1.0.0"
DEFAULT_ALIVE = """
**[TomrisUserBot](https://t.me/TomrisUserBot)**

**Bot Version:** {ver}
**Yüklü Modül Sayısı:** {modules}
**Bot Kurulma Zamanı:** {zaman}
"""
