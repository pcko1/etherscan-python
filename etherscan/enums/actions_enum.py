from dataclasses import dataclass


@dataclass(frozen=True)
class ActionsEnum:
    BALANCE_HISTORY: str = "balancehistory"
    BALANCE_MULTI: str = "balancemulti"
    BALANCE: str = "balance"
    GET_ABI: str = "getabi"
    GET_MINED_BLOCKS: str = "getminedblocks"
    GET_SOURCE_CODE: str = "getsourcecode"
    GET_STATUS: str = "getstatus"
    GET_TX_RECEIPT_STATUS: str = "gettxreceiptstatus"
    TOKEN_BALANCE: str = "tokenbalance"
    TOKEN_SUPPLY: str = "tokensupply"
    TOKENNFTTX: str = "tokennfttx"
    TOKENTX: str = "tokentx"
    TXLIST_INTERNAL: str = "txlistinternal"
    TXLIST: str = "txlist"

