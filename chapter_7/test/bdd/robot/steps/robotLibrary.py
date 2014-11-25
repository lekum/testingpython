from webtest import TestApp
from chapter_7.bank_app.app import app, BANK
from chapter_7.bank.account import Account

class robotLibrary(object):

    def __init__(self):
        self.browser = None
        self.response = None
        self.form_response = None

    def Create_Account(self, account_number, balance):
        a = Account(account_number, balance)
        BANK.add_account(a)

    def Visit_Homepage(self):
        self.browser = TestApp(app)
        self.response = self.browser.get('http://localhost:5000/')
        assert self.response.status_code == 200

    def Enter_Account(self, account_number):
        form = self.response.forms['account-form']
        form['account_number'] = account_number
        self.form_response = form.submit()
        assert self.form_response.status_code == 200

    def Get_Balance(self, expected_balance):
        assert "Balance: {}".format(expected_balance) in self.form_response.text
