import os
from dotenv import load_dotenv
import requests
from helpers import ResponseValidator

load_dotenv()


class BaseRequestHandler:
    def __init__(self):
        self.base_url = os.getenv("REQUEST_URL")
        self.headers = {'Accept': '*/*', 'Content-Type': 'application/json'}

    def _send_request(self, method: str, endpoint: str, payload: str = '',
                      expected_codes: list[int] = [200]) -> requests.Response:
        full_url = self.base_url + endpoint
        response = requests.request(
            method=method,
            url=full_url,
            headers=self.headers,
            data=payload
        )
        ResponseValidator.check_status_code(response, expected_codes)
        return response
