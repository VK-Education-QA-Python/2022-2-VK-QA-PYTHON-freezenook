from selenium.webdriver.common.by import By


class BaseLocators:
    # Локаторы разделов
    PROFILE_SECTION = (By.XPATH, './/*[contains(@class, "center-module-profile")]')
    TOOLS_SECTION = (By.XPATH, './/*[contains(@class, "center-module-tools")]')
    PROFILE_SECTION_LOCATOR = (By.XPATH, './/*[contains(@class, "profile-contact-info")]')
    TOOLS_SECTION_LOCATOR = (By.XPATH, './/*[contains(@class, "feeds-module-page")]')


class LoginLocators(BaseLocators):
    #Локаторы для авторизации
    LOGIN_BUTTON = (By.XPATH, './/*[contains(@class, "responseHead-module-button")]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    AUTH_BUTTON = (By.XPATH, './/*[contains(@class, "authForm-module-button")]')
    AUTH_NOTIFY_WRAPPER = (By.XPATH, './/*[contains(@class, "notify-module-wrapper")]')

    #Локаторы для логаута
    PROFILE_BUTTON = (By.XPATH, './/*[contains(@class, "right-module-rightWrap")]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')


class ContactInfoLocators(BaseLocators):
    #Локаторы для внесения контактной информации
    FIO_FIELD = (By.XPATH, '//*[@data-name="fio"]//child::input')
    INN_FIELD = (By.XPATH, '//*[@data-name="ordInn"]//child::input')
    PHONE_FIELD = (By.XPATH, '//*[@data-name="phone"]//child::input')
    SUBMIT_INFO_BUTTON = (By.CLASS_NAME, 'button__text')
    SUBMIT_INFO_WRAPPER = (By.XPATH, './/*[@data-class-name="SuccessView"]')
