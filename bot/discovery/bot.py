import logging

from bot.config.settings import COMMUNITY_ENDPOINT


class DiscoveryBot:

    def __init__(self, api):

        self.api = api
        self.result = {}


    def find_community(self):

        logging.info(
            "Searching community..."
        )

        data = self.api.get(
            "/rest/v1/communities"
            "?select=*"
            f"&endpoint=eq.{COMMUNITY_ENDPOINT}"
        )

        if not data:

            logging.error(
                "Community not found"
            )

            return False


        community = data[0]

        self.result["community"] = {
            "id": community["id"],
            "name": community["name"],
            "endpoint": community["endpoint"]
        }


        logging.info(
            "Community found: %s",
            community["name"]
        )

        return True


    def check_membership(self):

        if not self.api.user_id:

            raise RuntimeError(
                "User not authenticated"
            )


        cid = self.result["community"]["id"]


        logging.info(
            "Checking membership..."
        )


        data = self.api.get(
            "/rest/v1/community_members"
            "?select=*"
            f"&community_id=eq.{cid}"
            f"&user_id=eq.{self.api.user_id}"
        )


        if data:

            self.result["membership"] = data[0]

            logging.info(
                "Membership found"
            )

            return True


        logging.warning(
            "User is not member of community"
        )

        return False

    def run(self):

        logging.info(
            "Starting discovery"
        )

        if not self.find_community():
            return None

        self.check_membership()

        logging.info(
            "Discovery finished"
        )

        return self.result