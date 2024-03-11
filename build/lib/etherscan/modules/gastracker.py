from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules


class GasTracker:
    @staticmethod
    def get_est_confirmation_time(gas_price: int) -> str:
        # NOTE: gas_price in wei, result in seconds
        url = (
            f"{fields.MODULE}"
            f"{modules.GASTRACKER}"
            f"{fields.ACTION}"
            f"{actions.GAS_ESTIMATE}"
            f"{fields.GAS_PRICE}"
            f"{gas_price}"
        )
        return url

    @staticmethod
    def get_gas_oracle() -> str:
        # NOTE: gas_price in wei, result in seconds
        url = (
            f"{fields.MODULE}"
            f"{modules.GASTRACKER}"
            f"{fields.ACTION}"
            f"{actions.GAS_ORACLE}"
        )
        return url
