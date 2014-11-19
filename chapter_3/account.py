import requests

class ConnectionError(Exception):
    pass

class Account:

    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id_num):
        try:
            result = self.di.get(id_num)
        except ConnectionError:
            result =  "Connection error ocurred. Try again."
        return result

    def get_current_balance(self, id_num):
        return requests.get("http://some-account-uri/%s" % id_num)
