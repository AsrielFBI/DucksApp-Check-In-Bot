from pathlib import Path
import os

from dotenv import load_dotenv

BOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(
    BOT_DIR / "config" / ".env"
)

BASE_URL = os.getenv(
    "DUCK_BASE_URL"
)

EMAIL = os.getenv(
    "DUCK_EMAIL"
)

PASSWORD = os.getenv(
    "DUCK_PASSWORD"
)

ANON_KEY = os.getenv(
    "DUCK_ANON_KEY"
)

COMMUNITY_ENDPOINT = os.getenv(
    "DUCK_COMMUNITY_ENDPOINT"
)


# Datos generados
DATA_DIR = BOT_DIR / "data"

DISCOVERY_FILE = DATA_DIR / "discovery_result.json"
ACTIVITY_FILE = DATA_DIR / "activity_result.json"