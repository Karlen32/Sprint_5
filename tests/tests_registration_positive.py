from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from helpers import generators



class TestRegistration:


    def test_registration(self, driver):

        email = generators.generate_random_email()
        password = generators.generate_random_password()
        driver.find_element(*RegistrationPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGOUT_BUTTON))