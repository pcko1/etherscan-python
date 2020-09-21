from dataclasses import dataclass


@dataclass(frozen=True)
class ModulesEnum:
    ACCOUNT: str = "account"
    CONTRACT: str = "contract"
    TRANSACTION: str = "transaction"
    TOKEN: str = "token"

