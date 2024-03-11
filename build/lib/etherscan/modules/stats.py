from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules


class Stats:
    @staticmethod
    def get_total_eth_supply() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_SUPPLY}"
        )
        return url

    @staticmethod
    def get_eth_last_price() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_PRICE}"
        )
        return url

    @staticmethod
    def get_eth_nodes_size(
        start_date: str, end_date: str, client_type: str, sync_mode: str, sort: str
    ) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.CHAIN_SIZE}"
            f"{fields.START_DATE}"
            f"{start_date}"
            f"{fields.END_DATE}"
            f"{end_date}"
            f"{fields.CLIENT_TYPE}"
            f"{client_type}"
            f"{fields.SYNC_MODE}"
            f"{sync_mode}"
            f"{fields.SORT}"
            f"{sort}"
        )
        return url
