from dataclasses import dataclass


@dataclass(frozen=True)
class ActionsEnum:
    BALANCE_HISTORY: str = "balancehistory"
    BALANCE_MULTI: str = "balancemulti"
    BALANCE: str = "balance"
    GET_MINED_BLOCKS: str = "getminedblocks"
    TOKENNFTTX: str = "tokennfttx"
    TOKENTX: str = "tokentx"
    TXLIST_INTERNAL: str = "txlistinternal"
    TXLIST: str = "txlist"

