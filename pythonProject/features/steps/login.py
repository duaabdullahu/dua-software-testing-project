from behave import *
from hamcrest import assert_that, equal_to


@then("the user should be logged in successfully with the email: {email}")
def step_impl(context, email):
    assert_that(*context.homepage.navigation_buttons["Account"], equal_to(email))


@then("the '{errorMessage}' is shown")
def step_impl(context, errorMessage):
    assert_that(context.homepage.get_error_message(), equal_to(errorMessage))
