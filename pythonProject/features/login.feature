Feature: DemoWebshop Login

  Background:
    Given the home page is opened
    And the 'Login' button is clicked

  Scenario: Successful Login Attempt
    Given the 'Email' field is filled with 'dua@gmail.com'
    And the 'Password' field is filled with '123456'
    And the 'Login Form' button is clicked
    Then the user should be logged in successfully with the email: 'dua@gmail.com'
    And the 'Log Out' button is clicked

  Scenario Outline: Unsuccessful Login Attempt
    Given the 'Email' field is filled with '<email>'
    And the 'Password' field is filled with '<password>'
    And the 'Login Form' button is clicked
    Then the '<errorMessage>' is shown
    Examples:
    |email|password|errorMessage|
    |dua@gmail.com|1234565688|Login was unsuccessful. Please correct the errors and try again.|
    |bob@gmail.com|1232343545|Login was unsuccessful. Please correct the errors and try again.|
    |washington@gmail.com|34564567567|Login was unsuccessful. Please correct the errors and try again.|
    |helena@gmail.com    |345345645765|Login was unsuccessful. Please correct the errors and try again.|
    |michael@gmail.com   |23445676787 |Login was unsuccessful. Please correct the errors and try again.|
    |donaldtrump@gmail.com|45645645   |Login was unsuccessful. Please correct the errors and try again.|
    |kamala@gmail.com     |12342345645|Login was unsuccessful. Please correct the errors and try again.|


