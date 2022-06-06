from datetime import datetime

import requests
from behave import given, when, then

from src.utils import response_handler
from src.utils.settings_parser import settings

base_url = settings.base_url
api_key = settings.api_key
api_secret = settings.api_secret


@when(u'I retrieve server time')
def step_impl(context):
    context.response = requests.get(base_url + '/0/public/Time')


@then(u'Server time should have {time_format} time format')
def step_impl(context, time_format):
    try:
        datetime.strptime(context.response.json()['result']['rfc1123'], time_format)
    except ValueError:
        raise ValueError(f"Incorrect data format, should be {time_format}")


@given(u'I am a user')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given I am a user')
    pass


@then(u'I should get {code} status code')
def step_impl(context, code):
    actual_code = response_handler.status_code(context.response)
    assert actual_code == code, 'Invalid status code, expected %s, actual code is %s' % (code, actual_code)
