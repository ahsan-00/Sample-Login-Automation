# pages/signup_page.py
from.base_page import BasePage
from selenium.webdriver.common.by import By

class SignupPage(BasePage):
    URL = "/auth/register"
    EMAIL_INPUT = (By.XPATH, "//label[@class='v-label v-field-label']")
    Create_Account_BUTTON = (By.XPATH, "//span[normalize-space()='Create Account']")

    def fill_signup_form(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def click_signup_button(self):
        self.click(self.Create_Account_BUTTON)