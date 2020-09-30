import requests


class ResponseParser:
    @staticmethod
    def parse(response: requests.Response):
        content = response.json()
        result = content["result"]
        if "status" in content.keys():
            status = bool(int(content["status"]))
            message = content["message"]
            assert status, f"{result} -- {message}"
        else:
            # GETH or Parity proxy msg format
            # TODO: see if we need those values
            jsonrpc = content["jsonrpc"]
            cid = int(content["id"])
        return result
