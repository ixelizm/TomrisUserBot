from requests import get
import os, sys

def time_formatter(seconds, short=True):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + (" gün, " if not short else "g, ")) if days else "") + \
        ((str(hours) + (" saat, " if not short else "s, ")) if hours else "") + \
        ((str(minutes) + (" dakika, " if not short else "d, ")) if minutes else "") + \
        ((str(seconds) + (" saniye, " if not short else "s, ")) if seconds else "")
    return tmp[:-2] + " önce"





def update_init():
    response = get(UPSTREAM_URL)
    content = response.json()
    for file_name, file_content in content.items():
        with open(f"userbot/plugins/{file_name}.py", "w", encoding = "utf8") as file:
            file.write(file_content)
    args = [sys.executable, "main.py"]
    os.execle(sys.executable, *args, os.environ)
