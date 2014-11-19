import unittest

from unittest.mock import Mock, patch
from .. import account

class TestAccount(unittest.TestCase):

    def test_account_returns_data_for_id_1(self):
        account_data = {"id": "1", "name": "test"}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        account_ = account.Account(mock_data_interface)
        self.assertEquals(account_data, account_.get_account(1))

    def test_account_when_connect_exception_raised(self):
        mock_data_interface = Mock()
        mock_data_interface.get.side_effect = account.ConnectionError()
        account_ = account.Account(mock_data_interface)
        self.assertEqual("Connection error ocurred. Try again.",
                         account_.get_account(1))

    @patch.object(account, 'requests')
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        mock_requests.get.return_value = '500'
        account_ = account.Account(Mock())
        self.assertEqual('500', account_.get_current_balance(1))
