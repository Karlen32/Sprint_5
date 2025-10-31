import pytest
import random
from selenium import webdriver



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    return f"test_{random.randint(1000000000, 9999999999)}@gmail.com"

@pytest.fixture
def random_password():
    return f"test_{random.randint(1000000000, 9999999999)}"

@pytest.fixture
def login():
    email = "karlen000@gmail.com"
    password = "asd123"
    return email, password

@pytest.fixture
def ads_book_data():
    TITLE = f"Test Book {random.randint(1000, 9999)}"
    DESCRIPTION = f"Test Description {random.randint(1000, 9999)}"
    PRICE = "55000"
    return TITLE, DESCRIPTION, PRICE




