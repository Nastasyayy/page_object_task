from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL) # найти поле для почты
        email_input.send_keys(email) # ввести почту
        pass1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1) # найти поле пароля
        pass1_input.send_keys(password) # ввести пароль
        pass2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2) # найти поле повтора
        pass2_input.send_keys(password) # ввести тот же пароль
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON) # найти кнопку регистрации
        button.click() # нажать кнопку регистрации

    def should_be_registered(self):
        # реализуйте проверку, что вы были зарегистрированны
        assert self.is_element_present(*LoginPageLocators.REGISTER_MESSAGE), "User was not register"

