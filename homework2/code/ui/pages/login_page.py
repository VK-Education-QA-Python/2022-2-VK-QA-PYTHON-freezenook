from ui.locators import basic_locators
from ui.pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    locators = basic_locators.LoginPageLocators()
    url = 'https://target-sandbox.my.com/'

    @allure.step('Authorization')
    def login(self, login, password):
        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()

        self.type_field(self.locators.EMAIL_FIELD, login)
        self.type_field(self.locators.PASSWORD_FIELD, password)

        auth_button = self.find(self.locators.AUTH_BUTTON)
        auth_button.click()

    @allure.step('Logging out')
    def logout(self):
        profile_button = self.find(self.locators.PROFILE_BUTTON)
        profile_button.click()
        logout_button = self.find(self.locators.LOGOUT_BUTTON)
        try:
            logout_button.click()
        except:
            logout_button.click()
