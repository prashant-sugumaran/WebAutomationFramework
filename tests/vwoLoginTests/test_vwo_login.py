import time

import allure
import pytest
from selenium import webdriver

from tests.constants.constants import Constants
from tests.page_objects.DashboardPage import DashboardPage
from tests.page_objects.LoginPage import LoginPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(usr="admin@admin@gmail.com",pwd="admin")
    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(usr="test1@thetestingacademy.com",pwd="Welcome@123")
    time.sleep(10)
    dashboardPage = DashboardPage(driver)
    assert "Dashboard" in driver.title
    #assert "Aman" in dashboardPage.user_logged_in_text()