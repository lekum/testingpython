from behave import given
from chapter_6.bank_app.app import app
from webtest import TestApp

@given('I visit the homepage')
def step_impl(context):
    browser = TestApp(app)
    response = browser.get('http://localhost:5000/')
    assert response.status_code == 200
    assert response.text == "Hello World!"
