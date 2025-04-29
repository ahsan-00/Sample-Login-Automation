from pages.forgot_password_page import ForgotPasswordPage
from selenium import webdriver
from config.settings import Settings

class TestForgotPassword:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.forgot_password_page = ForgotPasswordPage(self.driver)

    def test_forgot_password(self):
        self.forgot_password_page.driver.get(Settings.BASE_URL + self.forgot_password_page.URL)
        self.forgot_password_page.fill_forgot_password_form("test@example.com")
        self.forgot_password_page.click_send_reset_link_button()
        assert self.forgot_password_page.driver.title == "Forgot Password Success"

    def teardown_method(self):
        self.driver.quit()