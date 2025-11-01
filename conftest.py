import pytest
from selenium import webdriver
from data.urls import Urls
from data import test_data
from helpers import generators




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_data():
    return test_data.LOGIN_EMAIL, test_data.LOGIN_PASSWORD


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




