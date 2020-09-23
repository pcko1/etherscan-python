from unittest import TestCase
import json

from etherscan.client import Client

_CONFIG_PATH = "test/configs/stable.json"
_API_KEY = "3PTZ5UHY7I9GGD74FJY6SXYS6JSVY295E5"


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


class TestModule(TestCase):
    _MODULE = ""

    def test_methods(self):
        print(f"\nMODULE: {self._MODULE}")
        config = load(_CONFIG_PATH)
        client = Client.from_config(_CONFIG_PATH, _API_KEY)
        for fun, v in config.items():
            if not fun.startswith("_"):
                if v["module"] == self._MODULE:
                    res, status, msg = getattr(client, fun)(**v["kwargs"])
                    print(f"METHOD: {fun}, STATUS: {status}")


class TestAccounts(TestModule):
    _MODULE = "accounts"


class TestContracts(TestModule):
    _MODULE = "contracts"


class TestTokens(TestModule):
    _MODULE = "tokens"


class TestTransactions(TestModule):
    _MODULE = "transactions"
