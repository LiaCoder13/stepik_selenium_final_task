from .base_page import BasePage
from .locators import LoginPageLocators
 
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
 
    def should_be_login_url(self):
        assert self.browser.current_url.find("login") != -1, "Login url is not correct"
 
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
 
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
         self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
         self.browser.find_element(*LoginPageLocators.REG_PASSWORDD1).send_keys(password)
         self.browser.find_element(*LoginPageLocators.REG_PASSWORDD2).send_keys(password)
         self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()