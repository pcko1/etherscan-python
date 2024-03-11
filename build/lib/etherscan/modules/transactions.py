from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules


class Transactions:
    @staticmethod
    def get_contract_execution_status(txhash: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_tx_receipt_status(txhash: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.TRANSACTION}"
            f"{fields.ACTION}"
            f"{actions.GET_TX_RECEIPT_STATUS}"
            f"{fields.TXHASH}"
            f"{txhash}"
        )
        return url
