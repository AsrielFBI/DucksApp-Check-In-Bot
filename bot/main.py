import json
import logging

from bot.core.api import DuckAPI
from bot.discovery.bot import DiscoveryBot
from bot.activity.bot import ActivityBot
from bot.utils.cleanup import clean_results
from bot.core.logger import setup_logging

from bot.config.settings import (
    BASE_URL,
    ANON_KEY,
    EMAIL,
    PASSWORD,
    DISCOVERY_FILE,
    ACTIVITY_FILE
)


def save_json(path, data):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


    logging.info(
        "Saved %s",
        path
    )



def main():
    setup_logging()
    logging.info(
        "Starting DucksApp Check-In Bot"
    )

    clean_results()

    api = DuckAPI(
        BASE_URL,
        ANON_KEY
    )

    api.login(
        EMAIL,
        PASSWORD
    )


    logging.info(
        "Authentication OK"
    )


    discovery_bot = DiscoveryBot(
        api
    )

    discovery_result = discovery_bot.run()

    if not discovery_result:

        logging.error(
            "Discovery failed, stopping"
        )

        return

    save_json(
        DISCOVERY_FILE,
        discovery_result
    )

    activity_bot = ActivityBot(
        api,
        discovery_result
    )

    activity_result = activity_bot.run()

    save_json(
        ACTIVITY_FILE,
        activity_result
    )

    logging.info(
        "Bot finished successfully"
    )

if __name__ == "__main__":

    main()