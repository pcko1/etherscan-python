import json
from datetime import datetime
import time

import os
from unittest import TestCase

from etherscan.etherscan import Etherscan

CONFIG_PATH = "etherscan/configs/{}-stable.json"
API_KEY = os.environ["API_KEY"]  # Encrypted env var by Travis


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


def dump(data, fname):
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)


class Case(TestCase):
    _MODULE = ""
    _NETS = ["MAIN", "KOVAN", "RINKEBY", "ROPSTEN"]

    def methods(self, net):
        print(f"\nNET: {net}")
        print(f"MODULE: {self._MODULE}")
        config = load(CONFIG_PATH.format(net))
        etherscan = Etherscan(API_KEY, net)
        for fun, v in config.items():
            if not fun.startswith("_"):  # disabled if _
                if v["module"] == self._MODULE:
                    res = getattr(etherscan, fun)(**v["kwargs"])
                    print(f"METHOD: {fun}, RTYPE: {type(res)}")
                    # Create log files (will update existing ones)
                    fname = f"logs/standard/{net}-{fun}.json"
                    log = {
                        "method": fun,
                        "module": v["module"],
                        "kwargs": v["kwargs"],
                        "log_timestamp": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                        "res": res,
                    }
                    dump(log, fname)
                    time.sleep(0.5)

    def test_net_methods(self):
        for net in self._NETS:
            self.methods(net)


class TestAccounts(Case):
    _MODULE = "accounts"


class TestBlocks(Case):
    _MODULE = "blocks"


class TestContracts(Case):
    _MODULE = "contracts"


class TestGasTracker(Case):
    _MODULE = "gastracker"


class TestPro(Case):
    _MODULE = "pro"


class TestProxy(Case):
    _MODULE = "proxy"


class TestStats(Case):
    _MODULE = "stats"


class TestTokens(Case):
    _MODULE = "tokens"


class TestTransactions(Case):
    _MODULE = "transactions"
