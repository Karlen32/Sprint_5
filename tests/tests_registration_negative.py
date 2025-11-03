from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from data.texts import RegistrationTexts
from turtle import color



class TestRegistrationNegative:

    def test_registration_invalid_email(self, driver, random_user):

        _, password = random_user
        driver.find_element(*RegistrationPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("karlen#gmail.com")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)).text
        assert error == RegistrationTexts.ERROR_MESSAGE


        email_field = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        email_y = email_field.location["y"]
        error_y = error_message.location["y"]
        difference = error_y - email_y
        assert 10 < difference < 60


        error_fields = driver.find_elements(*RegistrationPageLocators.RED_BORDER)
        assert color in error_fields == RegistrationTexts.ERROR_FIELD_COLOR_HEX or RegistrationTexts.ERROR_FIELD_COLOR_RGBA




    def test_registration_existing_user(self, driver):
        driver.find_element(*RegistrationPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("Karlen27@gmail.com")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("asd123")
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys("asd123")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        assert error.text == RegistrationTexts.ERROR_MESSAGE


        email_field = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        email_y = email_field.location["y"]
        error_y = error_message.location["y"]
        difference = error_y - email_y
        assert 10 < difference < 60


        error_fields = driver.find_elements(*RegistrationPageLocators.RED_BORDER)
        assert color in error_fields == RegistrationTexts.ERROR_FIELD_COLOR_HEX or RegistrationTexts.ERROR_FIELD_COLOR_RGBA

    
