import requests


class ResponseParser:
    @staticmethod
    def _get_content(response: requests.Response):
        return response.json()

    @staticmethod
    def get_status(response: requests.Response):
        c = ResponseParser._get_content(response)
        return int(c["status"])

    @staticmethod
    def get_message(response: requests.Response):
        c = ResponseParser._get_content(response)
        return c["message"]

    @staticmethod
    def get_result(response: requests.Response):
        c = ResponseParser._get_content(response)
        return c["result"]
