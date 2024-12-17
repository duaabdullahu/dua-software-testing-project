import time

from behave import *
from hamcrest import assert_that, equal_to


@given("the '{item}' is added to the cart")
def step_impl(context, item):
    context.homepage.add_to_cart(item)
    time.sleep(5)


@step("a new billing address button is clicked")
def step_impl(context):
    context.homepage.select_new_address()


@step("the country selected is Albania")
def step_impl(context):
    context.homepage.select_country_albania()


@then("the price should read '{total}'")
def step_impl(context, total):
    assert_that(context.homepage.get_total(), equal_to(total))


@then("the order should be successfully placed")
def step_impl(context):
    assert_that(context.homepage.driver.current_url, equal_to('https://demowebshop.tricentis.com/checkout/completed/'))


@given("the user searches for '{item}'")
def step_impl(context, item):
    context.homepage.search_for(item)


@then("the 'Computing and Internet' is in the cart")
def step_impl(context):
    assert_that(context.homepage.driver.current_url, equal_to('https://demowebshop.tricentis.com/cart'))
    assert_that(context.homepage.get_total(), equal_to("10.00"))


@step("the 'Quantity' field is cleared")
def step_impl(context):
    context.homepage.clear_quantity()