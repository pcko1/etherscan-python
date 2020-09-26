[![Build Status](https://travis-ci.com/pcko1/etherscan-python.svg?branch=master)](https://travis-ci.com/pcko1/etherscan-python) 
[![codecov](https://codecov.io/gh/pcko1/etherscan-python/branch/master/graph/badge.svg)](https://codecov.io/gh/pcko1/etherscan-python)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-385/)

![GitHub](https://img.shields.io/github/license/pcko1/etherscan-python)

# etherscan-python

Minimal python API for [etherscan.io](etherscan.io).

## Installation

Assuming [conda](https://docs.conda.io/en/latest/miniconda.html) is already installed in your system, first create the environment:

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

___
Powered by [Etherscan.io APIs](https://etherscan.io/apis).
