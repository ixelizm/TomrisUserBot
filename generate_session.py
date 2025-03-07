from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# API bilgilerini gir
API_ID = int(input("API KEY: "))  # Kendi API ID'ni gir
API_HASH = input("API HASH: ")  # Kendi API HASH'ini gir

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    session_string = client.session.save()
    client.send_message("me", f"`{session_string}`")
    print(session_string)
