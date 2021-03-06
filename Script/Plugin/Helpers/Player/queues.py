from typing import Dict, List, Union

from motor.motor_asyncio import AsyncIOMotorClient as Bot
from Script.Config import MONGODB_URL as tmo


MONGODB_CLI = Bot(tmo)
db = MONGODB_CLI.program


QUEUE = {}

pytgdb = db.pytg

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
    chat = await pytgdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def remove_queue(chat_id: int):
    is_served = await yar_aisa_na_kar(chat_id)
    if not is_served:
        return
    return await pytgdb.delete_one({"chat_id": chat_id})

