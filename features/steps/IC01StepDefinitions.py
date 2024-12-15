from behave import given, when, then

@given('the meter is connected over serial port')
def connect_meter(context):
    if context.data['is connected'] == False:
        context.data['dlms agent'].connect()
        context.data['is connected'] = True

@when('"{obis}" is read')
def read_obis(context, obis):
    context.data['obis value'] = context.data['dlms agent'].readObject(obis)

@then('actual value matches with "{expected_value}"')
def compare_values(context, expected_value):
    assert (context.data['obis value'] == expected_value)
    