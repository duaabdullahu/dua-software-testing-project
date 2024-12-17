from datetime import datetime

from behave import *
from hamcrest import assert_that, equal_to


@step("the home page is opened")
def step_impl(context):
    context.homepage.open_page()


@step("the '{button}' button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)


@given("the '{gender}' gender is selected")
def step_impl(context, gender):
    context.homepage.click_form_button(gender)


@step("the '{field}' field is filled with '{text}'")
def step_impl(context, field, text):
    field = '' if field == '[blank]' else field
    text = '' if text == '[blank]' else text
    context.homepage.fill_out_field(field, text)


@step("the email field is filled")
def step_impl(context):
    email = f"tester_{datetime.now().strftime('%Y%m%d%H%M%S')}@gmail.com"
    context.homepage.fill_out_email(email)


@then("the registration is successful")
def step_impl(context):
    assert_that(context.homepage.driver.current_url, equal_to('https://demowebshop.tricentis.com/registerresult/1'))


