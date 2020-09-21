from dataclasses import dataclass


@dataclass(frozen=True)
class ConstantsEnum:
    PREFIX = "https://api.etherscan.io/api?"
    MODULE = "module="
    ACTION = "&action="
    CONTRACT_ADDRESS = "&contractaddress="
    ADDRESS = "&address="
    OFFSET = "&offset="
    PAGE = "&page="
    SORT = "&sort="
    BLOCK_TYPE = "&blocktype="
    TO = "&to="
    VALUE = "&value="
    DATA = "&data="
    POSITION = "&position="
    HEX = "&hex="
    GAS_PRICE = "&gasPrice="
    GAS = "&gas="
    START_BLOCK = "&startblock="
    END_BLOCK = "&endblock="
    BLOCKNO = "&blockno="
    TXHASH = "&txhash="
    TAG = "&tag="
    BOOLEAN = "&boolean="
    INDEX = "&index="
    API_KEY = "&apikey="
