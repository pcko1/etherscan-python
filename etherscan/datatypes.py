from etherscan.enums.messages_enum import MessagesEnum as msgs

_CONTRACT_LEN = 42
_TX_LEN = 66
_WALLET_LEN = 42


class BaseAddress:
    def __init__(self):
        self._address = ""
        self._maxlen = 0

    def _check_0x(self, address: str):
        if address[:2] != "0x":
            raise ValueError(msgs.INVALID_ADDRESS)
        return address

    def _check_len(self, address: str):
        if len(address) != self._maxlen:
            raise ValueError(msgs.INVALID_ADDRESS)
        return address

    def __repr__(self):
        return self._address

    def __str__(self):
        return self._address

    def __add__(self, val: str):
        return self._address + val

    def __len__(self):
        return len(self._address)


class ContractAddress(BaseAddress):
    def __init__(self, address: str):
        self._maxlen = _CONTRACT_LEN
        self._address = self._check_len(self._check_0x(address))


class TxHash(BaseAddress):
    def __init__(self, address: str):
        self._maxlen = _TX_LEN
        self._address = self._check_len(self._check_0x(address))


class WalletAddress(BaseAddress):
    def __init__(self, address: str):
        self._maxlen = _WALLET_LEN
        self._address = self._check_len(self._check_0x(address))

