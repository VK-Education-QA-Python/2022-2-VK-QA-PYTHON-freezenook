from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.XPATH, './/*[contains(@class, "responseHead-module-button")]')
EMAIL_FIELD = (By.NAME, 'email')
PASSWORD_FIELD = (By.NAME, 'password')
AUTH_BUTTON = (By.XPATH, './/*[contains(@class, "authForm-module-button")]')
PROFILE_BUTTON = (By.XPATH, './/*[contains(@class, "right-module-rightWrap")]')
LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
AUTH_NOTIFY_WRAPPER = (By.XPATH, './/*[contains(@class, "notify-module-wrapper")]')
