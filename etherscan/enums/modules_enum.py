from dataclasses import dataclass


@dataclass(frozen=True)
class ModulesEnum:
    ACCOUNT: str = "account"
    BLOCK: str = "block"
    CONTRACT: str = "contract"
    GASTRACKER: str = "gastracker"
    PROXY: str = "proxy"
    STATS: str = "stats"
    TOKEN: str = "token"
    TRANSACTION: str = "transaction"

