import logging
import logging.handlers
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SERVER_PORT = os.getenv('SERVER_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

COMPOUND_FREQUENCY_TYPE = {
    'monthly': 12,
    'dayly': 365,
    'weekly': 52,
    'quarterly': 4,
    'semiannually': 2,
    'annually': 1
}

FILE_NAME = Path('grpc_server').stem
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
