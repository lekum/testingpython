import unittest

from unittest.mock import Mock


class TestingMock(unittest.TestCase):
    
    def test_mock_method_returns(self):
        my_mock = Mock()
        my_mock.my_method.return_value = "hello"
        self.assertEqual("hello", my_mock.my_method())
