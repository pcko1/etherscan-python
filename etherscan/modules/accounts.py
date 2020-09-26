from functools import reduce
from typing import List

from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules
from etherscan.enums.tags_enum import TagsEnum as tags


class Accounts:
    @staticmethod
    def get_eth_balance(address: str) -> str:
        """Returns ether balance for a single wallet.

        :param address: Wallet address
        :type address: str
        :return: The url to get 
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url
        # r = requests.get(url)
        # return conversions.to_ticker_unit(parser.get_result(r))

    @staticmethod
    def get_eth_balance_multiple(addresses: List[str]) -> str:
        """Returns ether balance for a list of wallets. Max of 20 wallets at a time.

        :param addresses: List of wallets
        :type addresses: List[str]
        :return: The url to get
        :rtype: str
        """
        address_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), addresses)
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_MULTI}"
            f"{fields.ADDRESS}"
            f"{address_list}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url
        # r = requests.get(url)
        # return [conversions.to_ticker_unit(r["balance"]) for r in parser.get_result(r)]

    @staticmethod
    def get_normal_txs_by_address(
        address: str,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        """Returns the last 10k normal transactions for an address.

        :param address: Wallet address
        :type address: str
        :param startblock: Starting block, defaults to 0000
        :type startblock: int, optional
        :param endblock: Ending block, defaults to 99999999
        :type endblock: int, optional
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
        # last 10,000 txs only
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{address}"
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
        address: str,
        page: int,
        offset: int,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        """Returns the paginated normal transactions for an address.

        :param address: Wallet address
        :type address: str
        :param page: Page number
        :type page: int
        :param offset: Max records to return
        :type offset: int
        :param startblock: Starting block, defaults to 0000
        :type startblock: int, optional
        :param endblock: Ending block, defaults to 99999999
        :type endblock: int, optional
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST}"
            f"{fields.ADDRESS}"
            f"{address}"
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
        address: str,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        """Returns the last 10k internal transactions for an address.

        :param address: Wallet address
        :type address: str
        :param startblock: Starting block, defaults to 0000
        :type startblock: int, optional
        :param endblock: Ending block, defaults to 99999999
        :type endblock: int, optional
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{address}"
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
        address: str,
        page: int,
        offset: int,
        startblock: int = 0000,
        endblock: int = 99999999,
        sort: str = "asc",
    ) -> str:
        """Returns the paginated internal transactions for an address.

        :param address: Wallet address
        :type address: str
        :param page: Page number
        :type page: int
        :param offset: Max records to return
        :type offset: int
        :param startblock: Starting block, defaults to 0000
        :type startblock: int, optional
        :param endblock: Ending block, defaults to 99999999
        :type endblock: int, optional
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TXLIST_INTERNAL}"
            f"{fields.ADDRESS}"
            f"{address}"
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
    def get_internal_txs_by_txhash(txhash: str) -> str:
        """Returns the last 10k internal transactions for a transaction hash.

        :param txhash: Transaction hash
        :type txhash: str
        :return: The url to get
        :rtype: str
        """
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
        """Returns the last 10k paginated internal transactions for a block range.

        :param startblock: Starting block
        :type startblock: int
        :param endblock: Ending block
        :type endblock: int
        :param page: Page number
        :type page: int
        :param offset: Max records to return
        :type offset: int
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
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
        address: str, startblock: int = 0, endblock: int = 999999999, sort: str = "asc",
    ) -> str:
        """Returns the last 10k ERC20 token transfer events for an address.

        :param address: Wallet address
        :type address: str
        :param startblock: Starting block, defaults to 0
        :type startblock: int, optional
        :param endblock: Ending block, defaults to 999999999
        :type endblock: int, optional
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENTX}"
            f"{fields.ADDRESS}"
            f"{address}"
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
        address: str, startblock: int = 0, endblock: int = 999999999, sort: str = "asc",
    ) -> str:
        """Returns the last 10k ERC721 token transfer events for an address.

        :param address: Wallet address
        :type address: str
        :param startblock: Starting block, defaults to 0
        :type startblock: int, optional
        :param endblock: Ending block, defaults to 999999999
        :type endblock: int, optional
        :param sort: Sort results, defaults to "asc"
        :type sort: str, optional
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKENNFTTX}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.START_BLOCK}"
            f"{str(startblock)}"
            f"{fields.END_BLOCK}"
            f"{str(endblock)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_mined_blocks_by_address(address: str) -> str:
        """Returns list of blocks mined by an address.

        :param address: Wallet address
        :type address: str
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.GET_MINED_BLOCKS}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCK_TYPE}"
            f"blocks"
        )
        return url
