from functools import reduce
from typing import List

from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules
from etherscan.enums.tags_enum import TagsEnum as tags


class Pro:
    @staticmethod
    def get_hist_eth_balance_for_address_by_block_no(
        address: str, block_no: int
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.BALANCE_HISTORY}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )
        return url

    @staticmethod
    def get_daily_average_block_size(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_BLOCK_SIZE}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_block_count_and_rewards(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_BLK_COUNT}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_block_rewards(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_BLOCK_REWARDS}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_average_block_time(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_BLOCK_TIME}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_uncle_block_count_and_rewards(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_UNCLE_BLK_COUNT}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_hist_erc20_token_total_supply_by_contract_address_and_block_no(
        contract_address: str, block_no: int
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY_HISTORY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )
        return url

    @staticmethod
    def get_hist_erc20_token_account_balance_for_token_contract_address_by_block_no(
        contract_address: str, address: str, block_no: int
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_BALANCE_HISTORY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )
        return url

    @staticmethod
    def get_token_info_by_contract_address(contract_address: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.TOKEN}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_INFO}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
        )
        return url

    @staticmethod
    def get_daily_average_gas_limit(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_GAS_LIMIT}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_eth_daily_total_gas_used(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_GAS_USED}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_eth_daily_average_gas_price(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_GAS_PRICE}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_eth_daily_network_tx_fee(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_TXN_FEE}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_new_address_count(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_NEW_ADDRESS}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_network_utilization(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_NET_UTILIZATION}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_average_network_hash_rate(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_HASH_RATE}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_tx_count(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_TX}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_daily_average_network_difficulty(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.DAILY_AVG_NET_DIFFICULTY}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_eth_hist_daily_market_cap(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_DAILY_MARKET_CAP}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_eth_hist_price(
        start_date: int,
        end_date: int,
        sort: str,
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_DAILY_PRICE}"
            f"{fields.START_DATE}"
            f"{str(start_date)}"
            f"{fields.END_DATE}"
            f"{str(end_date)}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url
