from dataclasses import dataclass


@dataclass(frozen=True)
class TokensEnum:
    DEFAULT: str = ""
    WETH: str = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    LINK: str = "0x514910771af9ca656af840dff83e8264ecf986ca"
    OCEAN: str = "0x7AFeBBB46fDb47ed17b22ed075Cde2447694fB9e"
