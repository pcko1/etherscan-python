from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules


class Blocks:
    @staticmethod
    def get_block_reward_by_block_number(block_no: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_REWARD}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )
        return url

    @staticmethod
    def get_est_block_countdown_time_by_block_number(block_no: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_COUNTDOWN}"
            f"{fields.BLOCKNO}"
            f"{block_no}"
        )
        return url

    @staticmethod
    def get_block_number_by_timestamp(timestamp: int, closest: str) -> str:
        # NOTE: Supports UNIX timestamps in seconds
        url = (
            f"{fields.MODULE}"
            f"{modules.BLOCK}"
            f"{fields.ACTION}"
            f"{actions.GET_BLOCK_NUMBER_BY_TIME}"
            f"{fields.TIMESTAMP}"
            f"{timestamp}"
            f"{fields.CLOSEST}"
            f"{closest}"
        )
        return url
