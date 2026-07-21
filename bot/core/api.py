import logging
import requests


class DuckAPI:
    def __init__(self, base, anon_key):
        self.base = base.rstrip("/")
        self.anon_key = anon_key

        self.session = requests.Session()

        self.jwt = None
        self.user_id = None

    def login(self, email, password):
        logging.info(
            "Logging in..."
        )

        r = self.session.post(
            f"{self.base}/auth/v1/token?grant_type=password",
            headers={
                "apikey": self.anon_key,
                "Content-Type": "application/json"
            },
            json={
                "email": email,
                "password": password
            },
            timeout=15
        )

        r.raise_for_status()
        data = r.json()

        self.jwt = data["access_token"]
        self.user_id = data["user"]["id"]

        logging.info(
            "Login OK: %s",
            self.user_id
        )

        return self.user_id

    def headers(self):
        if not self.jwt:
            raise RuntimeError(
                "API client not authenticated"
            )

        return {
            "apikey": self.anon_key,
            "Authorization": f"Bearer {self.jwt}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        r = self.session.get(
            self.base + endpoint,
            headers=self.headers(),
            timeout=10
        )
        r.raise_for_status()

        return r.json()

    def post(self, endpoint, payload):
        r = self.session.post(
            self.base + endpoint,
            headers=self.headers(),
            json=payload,
            timeout=15
        )

        try:
            return r.json()

        except ValueError:

            return {
                "status_code": r.status_code,
                "text": r.text
            }