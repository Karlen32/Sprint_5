from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import test_data



class TestLogin:


    def test_login(self, driver):
        driver.find_element(*LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data.LOGIN_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data.LOGIN_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON)
        )
        


    def test_logout(self, login_user):
        login_user.find_element(*LoginPageLocators.LOGOUT_BUTTON).click()

        assert WebDriverWait(login_user, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON))
        

    