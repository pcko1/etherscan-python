from unittest import TestCase
import json

from etherscan.client import Client
from etherscan.utils.datatypes import ContractAddress, TxHash, WalletAddress

_CONFIG_PATH = "etherscan/configs/stable.json"
_API_KEY = "3PTZ5UHY7I9GGD74FJY6SXYS6JSVY295E5"


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


class Case(TestCase):
    _MODULE = ""

    def test_methods(self):
        print(f"\nMODULE: {self._MODULE}")
        config = load(_CONFIG_PATH)
        client = Client.from_config(_CONFIG_PATH, _API_KEY)
        for fun, v in config.items():
            if not fun.startswith("_"):
                if v["module"] == self._MODULE:
                    res, status, msg = getattr(client, fun)(**v["kwargs"])
                    print(f"METHOD: {fun}, RTYPE: {type(res)}, STATUS: {status}")


class TestAccounts(Case):
    _MODULE = "accounts"


class TestContracts(Case):
    _MODULE = "contracts"


class TestTokens(Case):
    _MODULE = "tokens"


class TestTransactions(Case):
    _MODULE = "transactions"
