from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CreateAdPageLocators, LoginPageLocators



def test_create_ad_unauthorized_user(driver):
    driver.find_element(*CreateAdPageLocators.CREATE_AD_BUTTON).click()
    login_prompt = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(CreateAdPageLocators.LOGIN_PROMPT)).text
    assert login_prompt == "Чтобы разместить объявление, авторизуйтесь"


def test_create_ad_authorized_user(driver, login, ads_book_data):
    driver.find_element(*LoginPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login[0])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login[1])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGOUT_BUTTON))


    driver.find_element(*CreateAdPageLocators.CREATE_AD_BUTTON).click()
    driver.find_element(*CreateAdPageLocators.TITLE_INPUT).send_keys(ads_book_data[0])
    driver.find_element(*CreateAdPageLocators.CATEGORY_BUTTON).click()
    driver.find_element(*CreateAdPageLocators.CATEGORY_OPTION_BOOKS).click()
    driver.find_element(*CreateAdPageLocators.CONDITION_NEW_RABIBUTTON).click()
    driver.find_element(*CreateAdPageLocators.CITY_BUTTON).click()
    driver.find_element(*CreateAdPageLocators.CITY_OPTION_EKATERINBURG).click()
    driver.find_element(*CreateAdPageLocators.DESCRIPTION_INPUT).send_keys(ads_book_data[1])
    driver.find_element(*CreateAdPageLocators.PRICE_INPUT).send_keys(ads_book_data[2])
    driver.find_element(*CreateAdPageLocators.SUBMIT_AD_BUTTON).click()
    driver.find_element(*CreateAdPageLocators.UPLOAD_IMAGE_BUTTON).click()


   
    book_image = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(CreateAdPageLocators.BOOK_IMAGE))
    
    driver.execute_script("arguments[0].scrollIntoView();", book_image)
    assert book_image.is_displayed()

    ad_city = driver.find_element(*CreateAdPageLocators.AD_CiTY)
    assert ad_city.text == "Казань"


    

