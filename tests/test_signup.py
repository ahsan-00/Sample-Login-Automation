# test_signup.py
from pages.signup_page import SignupPage
from selenium import webdriver
from config.settings import Settings
import unittest

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.signup_page = SignupPage(self.driver)

    def test_signup(self):
        self.signup_page.driver.get(Settings.BASE_URL + self.signup_page.URL)
        self.signup_page.fill_signup_form("test@example.com")
        self.signup_page.click_signup_button()
        assert self.signup_page.driver.title == "Signup Success"



    def tearDown(self):
        self.driver.quit()       
