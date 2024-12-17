Feature: DemoWebshop Register

  Background:
    Given the home page is opened
    And the 'Register' button is clicked

  Scenario Outline: Registering users with different genders
    Given the '<gender>' gender is selected
    And the 'First Name' field is filled with 'testname_first'
    And the 'Last Name' field is filled with 'testname_last'
    And the email field is filled
    And the 'Password' field is filled with 'test_password'
    And the 'Confirm Password' field is filled with 'test_password'
    And the 'Register User' button is clicked
    Then the registration is successful
    And the 'Log Out' button is clicked
    Examples:
    |gender|
    |Male  |
    |Female|
