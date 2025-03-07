from . import bot, LOGS
from importlib import import_module
from .plugins import ALL_MODULES

for module_name in ALL_MODULES:
  imported_module = import_module("userbot.plugins." + module_name)

bot.start()
me = bot.get_me()
uid = me.id
LOGS.info(f"Bot Aktif - {uid}")
bot.run_until_disconnected()
