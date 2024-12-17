from selenium.webdriver.common.by import By


class Homepage:
    PAGE_URL = "https://demowebshop.tricentis.com/"

    navigation_buttons = {
        "Register": (By.CLASS_NAME, "ico-register"),
        "Login": (By.CLASS_NAME, "ico-login"),
        "Shopping Cart": (By.CLASS_NAME, "ico-cart"),
        "Register User": (By.ID, "register-button"),
        "Log Out": (By.CLASS_NAME, "ico-logout"),
        "Terms of Service": (By.ID, "termsofservice"),
        "Account": (By.CLASS_NAME, "account"),
        "Login Form": (By.CLASS_NAME, "button-1.login-button"),
        "Billing Address": (By.XPATH, "//select[@id='billing-address-select']"),
        "Billing Address Country": (By.ID, "BillingNewAddress_CountryId"),
        "Continue": (By.XPATH, "//input[@value='Continue']"),
        "Confirm": (By.CLASS_NAME, "button-1 confirm-order-next-step-button"),
        "Checkout": (By.ID, "checkout"),
        "Search Button": (By.CLASS_NAME, "button-1.search-box-button"),
        "Remove": (By.NAME, "removefromcart"),
        "Update Shopping Cart": (By.NAME, "updatecart"),
    }

    form_buttons = {
        "Male": (By.ID, "gender-male"),
        "Female": (By.ID, "gender-female"),
    }

    text_fields = {
        "First Name": (By.ID, "FirstName"),
        "Last Name": (By.ID, "LastName"),
        "Email": (By.ID, "Email"),
        "Password": (By.ID, "Password"),
        "Confirm Password": (By.ID, "ConfirmPassword"),
        "City": (By.ID, "BillingNewAddress_City"),
        "Address 1": (By.ID, "BillingNewAddress_Address1"),
        "Zip Code": (By.ID, "BillingNewAddress_ZipPostalCode"),
        "Phone Number": (By.ID, "BillingNewAddress_PhoneNumber"),
        "Search Bar": (By.ID, "small-searchterms"),
        "Quantity": (By.XPATH, "//td[@class='qty nobr']//input[@type='text']"),
    }

    messages = {
        "Login Error": (By.CLASS_NAME, "message-error"),
        "Price Label": (By.CSS_SELECTOR, "span.product-price.order-total strong")
    }

    item_buttons = {
        "14.1-inch Laptop": (By.CLASS_NAME, "button-2.product-box-add-to-cart-button"),
        "Computing and Internet": (By.CLASS_NAME, "button-2.product-box-add-to-cart-button"),
    }

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def click_button(self, button):
        self.driver.find_element(*self.navigation_buttons[button]).click()

    def click_form_button(self, button):
        self.driver.find_element(*self.form_buttons[button]).click()

    def fill_out_field(self, field, text):
        self.driver.find_element(*self.text_fields[field]).send_keys(text)

    def fill_out_email(self, text):
        self.driver.find_element(*self.text_fields["Email"]).send_keys(text)

    def close_page(self):
        self.driver.quit()

    def get_current_url(self):
        return self.driver.current_url()

    def get_error_message(self):
        return self.driver.find_element(*self.messages["Login Error"]).text.split("\n")[0]

    def add_to_cart(self, item):
        self.driver.find_element(*self.item_buttons[item]).click()

    def select_new_address(self):
        self.driver.find_element(*self.navigation_buttons["Billing Address"]).click()
        self.driver.find_element(By.XPATH, "//option[text()='New Address']").click()

    def select_country_albania(self):
        self.driver.find_element(*self.navigation_buttons["Billing Address Country"]).click()
        self.driver.find_element(By.XPATH, f'//option[@value="87"]').click()

    def get_total(self):
        return self.driver.find_element(*self.messages["Price Label"]).text

    def search_for(self, item):
        self.driver.find_element(*self.text_fields["Search Bar"]).send_keys(item)
        self.driver.find_element(*self.navigation_buttons["Search Button"]).click()

    def clear_quantity(self):
        self.driver.find_element(*self.text_fields["Quantity"]).clear()