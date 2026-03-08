from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page,expect
from elements.button import Button
from elements.link import Link
import re

class LoginPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.login_button = Button(page,'login-page-login-button', 'Login')
        self.registration_link = Link(page,'login-page-registration-link', 'Link')

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))


