from dataclasses import dataclass


@dataclass(frozen=True)
class FieldsEnum:
    ACTION: str = "&action="
    ADDRESS: str = "&address="
    API_KEY: str = "&apikey="
    BLOCK_TYPE: str = "&blocktype="
    BLOCKNO: str = "&blockno="
    BOOLEAN: str = "&boolean="
    CONTRACT_ADDRESS: str = "&contractaddress="
    DATA: str = "&data="
    END_BLOCK: str = "&endblock="
    GAS_PRICE: str = "&gasPrice="
    GAS: str = "&gas="
    HEX: str = "&hex="
    INDEX: str = "&index="
    MODULE: str = "module="
    OFFSET: str = "&offset="
    PAGE: str = "&page="
    POSITION: str = "&position="
    PREFIX: str = "https://api.etherscan.io/api?"
    SORT: str = "&sort="
    START_BLOCK: str = "&startblock="
    TAG: str = "&tag="
    TO: str = "&to="
    TXHASH: str = "&txhash="
    VALUE: str = "&value="
