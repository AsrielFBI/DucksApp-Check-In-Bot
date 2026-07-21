import logging
from datetime import datetime, timezone


class ActivityBot:
    def __init__(self, api, discovery):
        self.api = api
        self.discovery = discovery
        self.result = {}


    def check_status(self):
        cid = self.discovery["community"]["id"]

        logging.info(
            "Checking checkin status..."
        )

        data = self.api.get(
            "/rest/v1/community_members"
            "?select=*"
            f"&community_id=eq.{cid}"
            f"&user_id=eq.{self.api.user_id}"
        )

        if not data:
            logging.warning(
                "No membership found"
            )
            self.result["status"] = "no_membership"

            return False

        membership = data[0]
        self.result["before"] = membership

        if membership.get("has_checkin_today"):
            logging.info(
                "Check-in already completed"
            )
            self.result["status"] = "already_done"

            return False
        
        logging.info(
            "Check-in available"
        )

        return True



    def execute_checkin(self):
        cid = self.discovery["community"]["id"]

        logging.info(
            "Executing check-in..."
        )

        payload = {
            "p_community_id": cid
        }

        self.result["checkin_request"] = payload

        data = self.api.post(
            "/rest/v1/rpc/daily_checkin",
            payload
        )

        self.result["checkin_response"] = data
        self.result["status"] = "success"

        logging.info(
            "Check-in completed"
        )

    def refresh_membership(self):
        cid = self.discovery["community"]["id"]

        data = self.api.get(
            "/rest/v1/community_members"
            "?select=*"
            f"&community_id=eq.{cid}"
            f"&user_id=eq.{self.api.user_id}"
        )

        if data:
            self.result["after"] = data[0]



    def run(self):

        logging.info(
            "Starting activity"
        )

        if self.check_status():
            self.execute_checkin()

        self.refresh_membership()
        self.result["timestamp"] = datetime.now(
            timezone.utc
        ).isoformat()

        logging.info(
            "Activity finished"
        )

        return self.result