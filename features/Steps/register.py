from behave import *


@given(u'I navigate to Register Page')
def step_impl(context):
    print("Inside - I navigate to Register Page")


@when(u'I enter mandatory fields')
def step_impl(context):
   print("Inside - I enter mandatory fields")


@when(u'I click on Continue button')
def step_impl(context):
    print("Inside - I click on Continue button")


@then(u'Account should get created')
def step_impl(context):
    print("Inside - Account should get created ")


@when(u'I enter all fields')
def step_impl(context):
    print("Inside - I enter all fields")


@then(u'Account should be created')
def step_impl(context):
    print("Inside - Account should be created")


@when(u'I enter details into all fields except email field')
def step_impl(context):
    print("Inside - I enter details into all fields except email field")


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    print("Inside - I enter existing accounts email into email field")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print("Inside - Proper warning message informing about duplicate account should be displayed")


@when(u'I dont enter anything into the fields')
def step_impl(context):
    print("Inside - I dont enter anything into the fields")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    print("Inside -Proper warning messages for every mandatory fields should be displayed ")