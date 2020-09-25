from etherscan.utils.datatypes import ContractAddress
from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules


class Contracts:
    @staticmethod
    def get_contract_abi(contract: ContractAddress) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_ABI}"
            f"{fields.ADDRESS}"
            f"{contract}"
        )
        return url

    @staticmethod
    def get_contract_source_code(contract: ContractAddress) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.CONTRACT}"
            f"{fields.ACTION}"
            f"{actions.GET_SOURCE_CODE}"
            f"{fields.ADDRESS}"
            f"{contract}"
        )
        return url
