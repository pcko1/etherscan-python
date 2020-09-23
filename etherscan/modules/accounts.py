from functools import reduce
from typing import List

from etherscan.utils.datatypes import TxHash, WalletAddress
from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules
from etherscan.enums.tags_enum import TagsEnum as tags


class Accounts:
    @staticmethod
    def get_eth_balance(wallet: WalletAddress) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url
        # r = requests.get(url)
        # return conversions.to_ticker_unit(parser.get_result(r))

    @staticmethod
    def get_eth_balance_multiple(wallets: List[WalletAddress]) -> str:
        # max 20 wallets
        wallet_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), wallets)
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_MULTI}"
            f"{fields.ADDRESS}"
            f"{wallet_list}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url
        # r = requests.get(url)
        # return [conversions.to_ticker_unit(r["balance"]) for r in parser.get_result(r)]

    @staticmethod
    def get_hist_eth_balance_by_block(wallet: WalletAddress, block: int) -> str:
        # throttled to 2 calls/sec
        # BUG: returns 'Error! Missing Or invalid Action name'
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_HISTORY}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.BLOCKNO}"
            f"{str(block)}"
        )
        return url

    @staticmethod
    def get_normal_txs_by_address(
        wallet: WalletAddress,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        # last 10,000 txs only
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_normal_txs_by_address_paginated(
        wallet: WalletAddress,
        page: int,
        offset: int,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_address(
        wallet: WalletAddress,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        # last 10,000 txs only
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_address_paginated(
        wallet: WalletAddress,
        page: int,
        offset: int,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_txhash(txhash: TxHash) -> str:
        # last 10,000 txs only
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_internal_txs_by_block_range_paginated(
        startblock: int, endblock: int, page: int, offset: int, sort: str = "asc",
    ) -> str:
        # last 10,000 txs only
        # BUG: returns empty message
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
            f"{fields.PAGE}"
            f"{str(page)}"
            f"{fields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_erc20_token_transfer_events_by_address(
        wallet: WalletAddress,
        startblock: int = 0,
        endblock: int = 999999999,
        sort: str = "asc",
    ) -> str:
        # last 10,000 txs only
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_erc721_token_transfer_events_by_address(
        wallet: WalletAddress,
        startblock: int = 0,
        endblock: int = 999999999,
        sort: str = "asc",
    ) -> str:
        # last 10,000 txs only
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_mined_blocks_by_address(wallet: WalletAddress) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{wallet}"
            f"{fields.BLOCK_TYPE}"
            f"blocks"
        )
        return url
