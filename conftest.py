import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import Urls
from data import test_data
from helpers import generators
from locators import LoginPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def random_user():
    email = generators.generate_random_email()
    password = generators.generate_random_password()
    return email, password


@pytest.fixture
def ads_book_data():
    title, description = generators.generate_book_data()
    price = test_data.DEFAULT_PRICE
    return title, description, price


@pytest.fixture
def login_user(driver):
    driver.find_element(*LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data.LOGIN_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data.LOGIN_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON)
    )
    return driver




