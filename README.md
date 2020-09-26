

# etherscan-python

A minimal python API for [etherscan.io](etherscan.io).

[![Build Status](https://travis-ci.com/pcko1/etherscan-python.svg?branch=master)](https://travis-ci.com/pcko1/etherscan-python) 
[![codecov](https://codecov.io/gh/pcko1/etherscan-python/branch/master/graph/badge.svg)](https://codecov.io/gh/pcko1/etherscan-python)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-385/)
![GitHub](https://img.shields.io/github/license/pcko1/etherscan-python)
___

Most of the free webhooks from the [Accounts](https://etherscan.io/apis#accounts), [Contracts](https://etherscan.io/apis#contracts), [Transactions](https://etherscan.io/apis#transactions) and [Tokens](https://etherscan.io/apis#tokens) modules are supported. Their example use-cases are summarized [here](https://api.etherscan.io/apis).

## Installation

Before proceeding, you should register an account on etherscan.io and generate a personal API key to use. 

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

``` bash
conda activate etherscan-python && bash run_tests.sh
````

## Usage

In `python`, create a client with your personal etherscan.io API key:

``` python
from etherscan.client import Client

api_key = YOUR_API_KEY
config_path = "etherscan/configs/stable.json"

client = Client.from_config(config_path, api_key)
```

Then you can call all available methods, e.g.:

``` python
client.get_eth_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")

> ('40891631566070000000000', 'OK')
```

___
Powered by [Etherscan.io APIs](https://etherscan.io/apis).
