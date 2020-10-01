# etherscan-python

A minimal, yet complete, python API for [etherscan.io](etherscan.io).

[![Build Status](https://travis-ci.com/pcko1/etherscan-python.svg?branch=master)](https://travis-ci.com/pcko1/etherscan-python) 
[![codecov](https://codecov.io/gh/pcko1/etherscan-python/branch/master/graph/badge.svg)](https://codecov.io/gh/pcko1/etherscan-python)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-385/)

![GitHub](https://img.shields.io/github/license/pcko1/etherscan-python)

___

All of the *free* GET endpoints from the following modules are provided:

* [Accounts](https://etherscan.io/apis#accounts)
* [Contracts](https://etherscan.io/apis#contracts)
* [Transactions](https://etherscan.io/apis#transactions)
* [Blocks](https://etherscan.io/apis#blocks)
* [GETH/Parity Proxy](https://etherscan.io/apis#proxy)
* [Tokens](https://etherscan.io/apis#tokens)
* [Gas Tracker](https://etherscan.io/apis#gastracker)
* [Stats](https://etherscan.io/apis#stats)

## Installation

Before proceeding, you should register an account on [etherscan.io](etherscan.io) and generate a personal API key to use. 

Assuming [conda](https://docs.conda.io/en/latest/miniconda.html) is already installed on your system, first create the environment:

``` bash
conda env create -f env.yml
```

Activate the environment:

``` bash
conda activate etherscan-python
```

Then, install the package:

``` bash
pip install .
```

## Run unittests

Test that everything looks OK on your end before proceeding:

``` bash
coverage run -m unittest discover && coverage report -m
````

This will regenerate the logs under `logs/` with the most recent results and the timestamp of the execution.

## Usage

In `python` , create a client with your personal etherscan.io API key:

``` python
from etherscan import Etherscan

api_key = YOUR_API_KEY
config_path = "etherscan/configs/stable.json"

eth = Etherscan.from_config(config_path, api_key)
```

Then you can call all available methods, e.g.:

``` python
eth.get_eth_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")

> '40891631566070000000000'
```

## Examples

Examples (arguments and results) for all methods may be found as JSON files [here](https://github.com/pcko1/etherscan-python/tree/master/logs).  For example, if you want to use the method `get_block_number_by_timestamp` , you can find the supported arguments and the format of its output in its respective [JSON file](logs/get_block_number_by_timestamp.json):

``` json
{
  "method": "get_block_number_by_timestamp",
  "module": "blocks",
  "kwargs": {
    "timestamp": "1578638524",
    "closest": "before"
  },
  "log_timestamp": "2020-09-30-15:39:18",
  "res": "9251482"
}
```

where `kwargs` refer to the required arguments and `res` refers to the expected result if you run:

``` python
eth.get_block_number_by_timestamp(timestamp="1578638524", closest="before")
```

**Disclaimer**: Those examples blindly use the arguments originally showcased [here](https://api.etherscan.io/apis) and the selected wallets/contracts do not reflect any personal views. You should refer to the same source for additional information regarding specific argument values.

## Issues

For problems regarding installing or using the package please open an [issue](https://github.com/pcko1/etherscan-python/issues). If you think that a newly-added method is missing, also open an issue as a feature request and I will do my best to add it. Kindly avoid disclosing potentially sensitive information such as your API keys or your wallet addresses.

___
Powered by [Etherscan.io APIs](https://etherscan.io/apis).
