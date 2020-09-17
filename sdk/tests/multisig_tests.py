import time
import unittest

from web3 import Web3

from sdk.kit import Kit
from sdk.tests import test_data


class TestMultiSigWrapper(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.kit = Kit('https://alfajores-forno.celo-testnet.org')
        self.multi_sig_wrapper = self.kit.base_wrapper.create_and_get_contract_by_name(
            'MultiSig')
        self.kit.wallet_add_new_key = test_data.pk1