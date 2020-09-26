import json
from functools import wraps

import requests

import etherscan
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.utils.parsing import ResponseParser as parser


class Client:
    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)

    @staticmethod
    def __run(func, api_key):
        # decorator to authorize and get urls
        def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{api_key}"
            )
            r = requests.get(url)
            return (parser.get_result(r), parser.get_status(r), parser.get_message(r))

        return wrapper

    @staticmethod
    def __check_status(func):
        # decorator to assert message status
        def wrapper(*args, **kwargs):
            res, status, msg = func(*args, **kwargs)
            assert bool(status), msg
            return (res, msg)

        return wrapper

    @classmethod
    def from_config(cls, config_path: str, api_key: str):
        config = cls.__load_config(config_path)
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(etherscan, v["module"]), func)
                setattr(cls, func, cls.__check_status(cls.__run(attr, api_key)))
        return cls
