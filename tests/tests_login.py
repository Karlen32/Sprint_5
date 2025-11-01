from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
import pytest


@pytest.mark.usefixtures("driver")
class TestLogin:


    def test_login(self, driver, login_data):

        email, password = login_data
        driver.find_element(*LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON))
        


    def test_logout(self, driver, login_data):

        email, password = login_data
        driver.find_element(*LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() 
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON))
        
        driver.find_element(*LoginPageLocators.LOGOUT_BUTTON).click() 
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON))
    