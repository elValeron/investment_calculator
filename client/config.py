import logging
import logging.handlers
import os

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', default='')


SERVER_PORT = os.getenv('SERVER_PORT')

FILE_NAME = Path('client').stem

LOG_DIR = os.path.expanduser(f'logs/{FILE_NAME}'+'.log')
os.makedirs(os.path.dirname(LOG_DIR), exist_ok=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    filename=LOG_DIR,
    maxBytes=5_000_000,
    encoding='utf-8',
    backupCount=3
)

formatter = logging.Formatter(
    '%(asctime)s, %(levelname)s, %(message)s, %(funcName)s, %(lineno)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
