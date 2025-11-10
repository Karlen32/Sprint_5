from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CreateAdPageLocators, LoginPageLocators
from data.texts import AdsTexts




class TestAds:

    def test_create_ad_unauthorized_user(self, driver):
        driver.find_element(*CreateAdPageLocators.CREATE_AD_BUTTON).click()
        login_prompt = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(CreateAdPageLocators.LOGIN_PROMPT)).text
        assert login_prompt == AdsTexts.LOGIN_PROMPT


    def test_create_ad_authorized_user(self, driver, login_user, ads_book_data):

        WebDriverWait(login_user, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON))
        

        title, description, price = ads_book_data
        driver.find_element(*CreateAdPageLocators.CREATE_AD_BUTTON).click()
        driver.find_element(*CreateAdPageLocators.TITLE_INPUT).send_keys(title)
        driver.find_element(*CreateAdPageLocators.CATEGORY_BUTTON).click()
        driver.find_element(*CreateAdPageLocators.CATEGORY_OPTION_BOOKS).click()
        driver.find_element(*CreateAdPageLocators.CONDITION_NEW_RABIBUTTON).click()
        driver.find_element(*CreateAdPageLocators.CITY_BUTTON).click()
        driver.find_element(*CreateAdPageLocators.CITY_OPTION_EKATERINBURG).click()
        driver.find_element(*CreateAdPageLocators.DESCRIPTION_INPUT).send_keys(description)
        driver.find_element(*CreateAdPageLocators.PRICE_INPUT).send_keys(price)
        driver.find_element(*CreateAdPageLocators.SUBMIT_AD_BUTTON).click()
        driver.find_element(*CreateAdPageLocators.UPLOAD_IMAGE_BUTTON).click()


    
        book_image = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(CreateAdPageLocators.BOOK_IMAGE))
        
        driver.execute_script("arguments[0].scrollIntoView();", book_image)
        assert book_image.is_displayed()

        ad_city = driver.find_element(*CreateAdPageLocators.AD_CiTY)
        assert ad_city.text == AdsTexts.AD_CITY


    

