from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page,expect

class LoginPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()


