from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):
    URL = "/forgot-password"
    EMAIL_INPUT = (By.NAME, "email")
    SEND_RESET_LINK_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_forgot_password_form(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def click_send_reset_link_button(self):
        self.click(self.SEND_RESET_LINK_BUTTON)