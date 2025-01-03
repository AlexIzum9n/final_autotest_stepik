from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "There is no login phrase in url adress"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "There is no register form"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.USER_EMAIL)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        user_password.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_ACCEPT)
        user_password2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()