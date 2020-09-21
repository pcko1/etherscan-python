from dataclasses import dataclass


@dataclass(frozen=True)
class ConstantsEnum:
    PREFIX: str = "https://api.etherscan.io/api?"
    MODULE: str = "module="
    ACTION: str = "&action="
    CONTRACT_ADDRESS: str = "&contractaddress="
    ADDRESS: str = "&address="
    OFFSET: str = "&offset="
    PAGE: str = "&page="
    SORT: str = "&sort="
    BLOCK_TYPE: str = "&blocktype="
    TO: str = "&to="
    VALUE: str = "&value="
    DATA: str = "&data="
    POSITION: str = "&position="
    HEX: str = "&hex="
    GAS_PRICE: str = "&gasPrice="
    GAS: str = "&gas="
    START_BLOCK: str = "&startblock="
    END_BLOCK: str = "&endblock="
    BLOCKNO: str = "&blockno="
    TXHASH: str = "&txhash="
    TAG: str = "&tag="
    BOOLEAN: str = "&boolean="
    INDEX: str = "&index="
    API_KEY: str = "&apikey="
