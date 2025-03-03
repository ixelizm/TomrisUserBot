from telethon import events
from userbot import bot


def tomris(**args):
    def decorator(func):
        async def wrapper(check):

            try:
                await func(check)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                pass
            else:
                pass
        
        bot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator