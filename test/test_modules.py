import json
from datetime import datetime
from unittest import TestCase

from etherscan.etherscan import Etherscan

_CONFIG_PATH = "etherscan/configs/stable.json"
_API_KEY = "3PTZ5UHY7I9GGD74FJY6SXYS6JSVY295E5"


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


def dump(data, fname):
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)


class Case(TestCase):
    _MODULE = ""

    def test_methods(self):
        print(f"\nMODULE: {self._MODULE}")
        config = load(_CONFIG_PATH)
        etherscan = Etherscan.from_config(_CONFIG_PATH, _API_KEY)
        for fun, v in config.items():
            if not fun.startswith("_"):  # disabled if _
                if v["module"] == self._MODULE:
                    res = getattr(etherscan, fun)(**v["kwargs"])
                    print(f"METHOD: {fun}, RTYPE: {type(res)}")
                    # Create log files (will update existing ones)
                    fname = f"logs/{fun}.json"
                    log = {
                        "method": fun,
                        "module": v["module"],
                        "kwargs": v["kwargs"],
                        "timestamp": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                        "res": res,
                    }
                    dump(log, fname)


class TestAccounts(Case):
    _MODULE = "accounts"


class TestBlocks(Case):
    _MODULE = "blocks"


class TestContracts(Case):
    _MODULE = "contracts"


class TestGasTracker(Case):
    _MODULE = "gastracker"


class TestProxy(Case):
    _MODULE = "proxy"


class TestStats(Case):
    _MODULE = "stats"


class TestTokens(Case):
    _MODULE = "tokens"


class TestTransactions(Case):
    _MODULE = "transactions"
