import time
from datetime import datetime

import requests
from behave import given, when, then

from src.utils import request_helper
from src.utils import response_handler, schema_loader
from src.utils.settings_parser import settings

base_url = settings.base_url
api_key = settings.api_key
api_secret = settings.api_secret
trading_pairs = settings.trading_pairs
otp = settings.otp


@when(u'I retrieve server time')
def retrieve_server_time(context):
    context.response = requests.get(base_url + '/0/public/Time')


@then(u'Server time should have {time_format} time format')
def assert_time_format(context, time_format):
    try:
        datetime.strptime(context.response.json()['result']['rfc1123'], time_format)
    except ValueError:
        raise ValueError(f"Incorrect data format, should be {time_format}")


@given(u'I am a user')
def step_impl(context):
    pass


@then(u'I should get {code} status code')
def assert_status_code(context, code):
    actual_code = response_handler.status_code(context.response)
    assert actual_code == code, 'Invalid status code, expected %s, actual code is %s' % (code, actual_code)


@when(u'I request public info about trading pair {pair}')
def step_impl(context, pair):
    pair_parameter = trading_pairs[pair]['request_parameter']
    context.response = requests.get(base_url + f'/0/public/AssetPairs?pair={pair_parameter}')


@then(u'Response data should be about {pair} trading pair')
def step_impl(context, pair):
    expected_altname = trading_pairs[pair]['altname']
    actual_altname = context.response.json()['result'][trading_pairs[pair]['request_parameter']]['altname']
    assert expected_altname == actual_altname, 'Unexpected trading pair in response, expected %s, actual pair %s' % (
        expected_altname, actual_altname)


@then("{name} json schema should be valid")
def step_impl(context, name):
    schema = schema_loader.get_json_schema(schema=name.lower())

    # check response corresponds to schema
    assert response_handler.validate_json(context.response, schema), 'Category list schema is not valid'


@given(u'I am an authenticated user')
def step_impl(context):
    pass


@when(u'I retrieve open orders')
def step_impl(context):
    # Construct the request and print the result
    context.response = request_helper.kraken_post_request(base_url, '/0/private/OpenOrders', {
        "nonce": str(int(1000 * time.time())),
        "otp": otp,
        "trades": True
    }, api_key, api_secret)


@then(u'I should get empty list of opened orders')
def step_impl(context):
    expected_list = {}
    assert context.response.json()['result']['open'] == expected_list, 'List of orders is not empty'
