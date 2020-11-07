from dataclasses import dataclass


@dataclass(frozen=True)
class ConfigsEnum:
    STABLE: str = "stable.json"