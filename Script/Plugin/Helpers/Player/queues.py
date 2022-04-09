from typing import Dict, List, Union
from Script.Plugin.Database import db


QUEUE = {}


def add_to_queue(chat_id, title, duration, ytlink, playlink, type, quality, thumb):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([title, duration, ytlink, playlink, type, quality, thumb])
        return int(len(chat_queue) - 1)
    else:
        QUEUE[chat_id] = [[title, duration, ytlink, playlink, type, quality, thumb]]


def get_queue(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        return chat_queue
    else:
        return 0


def pop_an_item(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.pop(0)
        return 1
    else:
        return 0



def clear_queue(chat_id):
    if chat_id in QUEUE:
        QUEUE.pop(chat_id)
        return 1
    else:
        return 0

    
async def yar_aisa_na_kar(chat_id: int) -> bool:
    chat = await db.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def remove_queue(chat_id: int):
    is_served = await yar_aisa_na_kar(chat_id)
    if not is_served:
        return
    return await db.delete_one({"chat_id": chat_id})

