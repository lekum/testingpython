import unittest

from chapter_6.bank.account import Account

class TestAccount(unittest.TestCase):

    def test_account_object_returns_current_balance(self):
        account = Account("001", 50)
        self.assertEquals(account.account_number, "001")
        self.assertEquals(account.balance, 50)
