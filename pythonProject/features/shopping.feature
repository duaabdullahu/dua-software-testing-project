Feature: DemoWebshop Shopping

  Background:
    Given the home page is opened
    And the 'Login' button is clicked
    And the 'Email' field is filled with 'dua@gmail.com'
    And the 'Password' field is filled with '123456'
    And the 'Login Form' button is clicked

  Scenario: Searching for a book and adding it to the cart and removing it from the cart
    Given the user searches for 'Computing and Internet'
    And the 'Computing and Internet' is added to the cart
    And the 'Shopping Cart' button is clicked
    Then the 'Computing and Internet' is in the cart
    And the 'Remove' button is clicked
    And the 'Update Shopping Cart' button is clicked
    And the 'Log Out' button is clicked

  Scenario: Adding a Laptop to the cart and increasing the quantity of items
    Given the user searches for '14.1-inch Laptop'
    And the '14.1-inch Laptop' is added to the cart
    And the 'Shopping Cart' button is clicked
    And the 'Quantity' field is cleared
    And the 'Quantity' field is filled with '2'
    And the 'Update Shopping Cart' button is clicked
    Then the price should read '3180.00'
    And the 'Remove' button is clicked
    And the 'Update Shopping Cart' button is clicked
    And the 'Log Out' button is clicked






