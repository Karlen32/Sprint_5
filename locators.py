from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'input_span') and text()='Ошибка']")
    RED_BORDER = (By.CSS_SELECTOR, ".input_inputError__fLUP9 input")


class LoginPageLocators:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'input_span') and text()='Логин или пароль неверны']")
    RED_BORDER = (By.CSS_SELECTOR, ".input_inputError__fLUP9 input")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")


class CreateAdPageLocators:
    CREATE_AD_BUTTON = (By.XPATH, "//button[normalize-space(text())='Разместить объявление']")
    LOGO = (By.CSS_SELECTOR, ".header_logo__yAp5Y")
    LOGIN_PROMPT = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    TITLE_INPUT = (By.NAME, "name")
    CATEGORY_BUTTON = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[1]")
    CATEGORY_OPTION_BOOKS = (By.XPATH, "//span[text()='Книги']")
    CONDITION_NEW_RABIBUTTON = (By.CSS_SELECTOR, "div.radioUnput_inputRegular__FbVbr")
    CITY_BUTTON = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]")
    CITY_OPTION_EKATERINBURG = (By.XPATH, "//span[text()='Казань']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    SUBMIT_AD_BUTTON = (By.XPATH, "//button[normalize-space()='Опубликовать']")
    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    BOOK_IMAGE = (By.CSS_SELECTOR, "img.picture")
    AD_CiTY = (By.CSS_SELECTOR, "div.about > h3.h3")
    
    