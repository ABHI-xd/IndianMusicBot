import time
import logging

from Script.assistant.TgCalls.Clients import indian

logging.basicConfig(
  filename=f'streambot-logs-{indian.id}.txt',
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("PyTgCalls").setLevel(logging.ERROR)

LOGGER = logging.getLogger(__name__)
