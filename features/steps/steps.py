from datetime import datetime

from behave import given, when, then

from src.entities.ApiClient import ApiClient, SecureApiClient
from src.utils import response_handler, schema_loader
from src.utils.settings_parser import settings

trading_pairs = settings.trading_pairs


@when(u'I retrieve server time')
def retrieve_server_time(context):
    context.response = context.client.get_server_time()


@then(u'Server time should have {time_format} time format')
def assert_time_format(context, time_format):
    try:
        datetime.strptime(context.response.json()['result']['rfc1123'], time_format)
    except ValueError:
        raise ValueError(f"Incorrect data format, should be {time_format}")


@given(u'I am a user')
def basic_user(context):
    context.client = ApiClient()


@then(u'I should get {code} status code')
def assert_status_code(context, code):
    actual_code = response_handler.status_code(context.response)
    assert actual_code == code, 'Invalid status code, expected %s, actual code is %s' % (code, actual_code)


@when(u'I request public info about trading pair {pair}')
def request_trading_pair(context, pair):
    pair_parameter = trading_pairs[pair]['request_parameter']
    context.response = context.client.get_trading_pair(pair_parameter)


@then(u'Response data should be about {pair} trading pair')
def assert_pair_response(context, pair):
    expected_altname = trading_pairs[pair]['altname']
    actual_altname = context.response.json()['result'][trading_pairs[pair]['request_parameter']]['altname']
    assert expected_altname == actual_altname, 'Unexpected trading pair in response, expected %s, actual pair %s' % (
        expected_altname, actual_altname)


@then("{name} json schema should be valid")
def validate_json_schema(context, name):
    schema = schema_loader.get_json_schema(schema=name.lower())

    # check response corresponds to schema
    assert response_handler.validate_json(context.response, schema), 'Category list schema is not valid'


@given(u'I am an authenticated user')
def authenticated_user(context):
    context.client = SecureApiClient()


@when(u'I retrieve open orders')
def retrieve_open_orders(context):
    context.response = context.client.retrieve_open_orders()


@then(u'I should get empty list of opened orders')
def assert_open_orders_empty(context):
    expected_list = {}
    assert context.response.json()['result']['open'] == expected_list, 'List of orders is not empty'
