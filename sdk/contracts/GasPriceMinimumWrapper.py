import sys

from web3 import Web3


class GasPriceMinimum:
    def __init__(self, web3: Web3, address: str, abi: list, wallet: 'Wallet' = None):
        self.web3 = web3
        self.address = address
        self._contract = self.web3.eth.contract(self.address, abi=abi)
        self.__wallet = wallet

    def get_price_minimum(self) -> int:
        return self._contract.functions.gasPriceMinimum().call()

    def get_gas_price_minimum(self, address: str) -> int:
        return self._contract.functions.getGasPriceMinimum(address).call()

    def target_density(self) -> int:
        return self._contract.functions.targetDensity().call()

    def adjustment_speed(self) -> int:
        return self._contract.functions.adjustmentSpeed().call()

    def get_config(self) -> dict:
        pass
