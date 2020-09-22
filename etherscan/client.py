import requests as req


class Client:
    def __init__(self, api_key: str):
        self.api_key = api_key

    # accounts
    def get_eth_balance(self, wallet: str):
        pass

    def get_eth_balance_multiple(self):
        pass

    def get_hist_eth_balance(self):
        # throttled to 2 calls/sec
        pass

    def get_normal_txs_by_address(self):
        pass

    def get_internal_txs_by_address(self):
        pass

    def get_internal_txs_by_txhash(self):
        pass

    def get_internal_txs_by_block_range(self):
        pass

    def get_erc20_transfer_events_by_address(self):
        pass

    def get_erc721_transfer_events_by_address(self):
        pass

    def get_mined_blocks_by_address(self):
        pass

