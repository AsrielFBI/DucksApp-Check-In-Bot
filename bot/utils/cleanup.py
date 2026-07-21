from pathlib import Path

from bot.config.settings import (
    DISCOVERY_FILE,
    ACTIVITY_FILE
)


def clean_results():

    for file in (
        DISCOVERY_FILE,
        ACTIVITY_FILE
    ):

        path = Path(file)

        if path.exists():
            path.unlink()