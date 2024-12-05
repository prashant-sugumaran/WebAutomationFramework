# Page Class
# Page Locators
# Page Actions
# Webdriver Init
# Custom Functions
# No Assertions
from selenium.webdriver.common.by import By

from tests.utils.common_utils import webdriver_wait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
    # forgot_password_button = (By.XPATH,"//button[text()='Forgot Password?']")
    free_trail = (By.XPATH, "//a[text()='Start a free trial']")

    # sso_login = (By.XPATH,"//button[text()='Sign in using SSO']")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trail(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username, timeout=5)
        return self.driver.find_element(*LoginPage.free_trail)

    def login_to_vwo(self, usr, pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()
        except Exception as e:
            print(e)

    def get_error_message_text(self):
        return self.get_error_message().text

    def click_free_trail(self):
        self.get_free_trail().click()
