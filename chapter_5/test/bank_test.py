import unittest

from ..bank import Bank 
from ..account import Account 

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_is_initially_empty(self):
        self.assertEquals({}, self.bank.accounts)
        self.assertEquals(len(self.bank.accounts), 0)

    def test_add_account(self):
        account_1 = Account("001", 50)
        self.bank.add_account(account_1)
        self.assertEquals(self.bank.get_account_balance("001"), 50)
