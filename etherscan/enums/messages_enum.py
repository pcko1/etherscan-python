from dataclasses import dataclass


@dataclass(frozen=True)
class MessagesEnum:
    METHOD_DISABLED: str = "This method is disabled for now."
    INVALID_ADDRESS: str = "This address is invalid."
