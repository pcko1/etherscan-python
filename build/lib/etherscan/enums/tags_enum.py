from dataclasses import dataclass


@dataclass(frozen=True)
class TagsEnum:
    ACCOUNT: str = "account"
    LATEST: str = "latest"
