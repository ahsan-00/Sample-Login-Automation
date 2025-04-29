from pages.login_page import LoginPage
from selenium import webdriver
from config.settings import Settings

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.login_page.driver.get(Settings.BASE_URL + self.login_page.URL)
        self.login_page.fill_login_form("test@example.com", "password123")
        self.login_page.click_login_button()
        assert self.login_page.driver.title == "Login Success"

    def teardown_method(self):
        self.driver.quit()