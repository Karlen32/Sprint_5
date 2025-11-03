from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestLogin:


    def test_login(self, login_user):

        assert WebDriverWait(login_user, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON))
        


    def test_logout(self, login_user):
        login_user.find_element(*LoginPageLocators.LOGOUT_BUTTON).click()

        assert WebDriverWait(login_user, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON))
        

    