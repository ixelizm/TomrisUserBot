from telethon.sync import TelegramClient
from logging import basicConfig, getLogger, INFO
from telethon.tl.functions.channels import JoinChannelRequest
from core.database import Environment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time, glob
from dotenv import load_dotenv
import os
from core.functions import time_formatter
load_dotenv("config.env")
basicConfig(format="%(asctime)s - @TomrisUserBot - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

bot = TelegramClient("tomris", API_KEY, API_HASH)

with bot:
    try:
        bot(JoinChannelRequest("@TomrisUserBot"))
        bot(JoinChannelRequest("@TomrisSupport"))
    except:
        pass
    me = bot.get_me()
    uid = me.id
    engine = create_engine('sqlite:///userbot.db', echo=True)

# Session oluştur
    Session = sessionmaker(bind=engine)
    session = Session()
    STARTED_TIME = session.query(Environment).first()
    if STARTED_TIME is None:
        started_time = time.time()
        new = Environment(started_time = started_time)
        session.add(new)
        session.commit()
        STARTED_TIME = started_time
    else:
        STARTED_TIME = STARTED_TIME.started_time
    LOGS.info(STARTED_TIME)
UPSTREAM_URL = "http://141.98.115.181:8080/"
VERSION = "V1.0.0"
zaman = ""
DEFAULT_ALIVE = """
**[TomrisUserBot](https://t.me/TomrisUserBot)**

**Bot Version:** {ver}
**Yüklü Modül Sayısı:** {modules}
**Bot Kurulma Zamanı:** {zaman}
"""