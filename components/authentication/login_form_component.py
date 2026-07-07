from playwright.sync_api import Page, expect
import allure
from elements.input import Input
from elements.text import Text

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page,'login-form-password-input','Password')
        self.wrong_email_or_password_alert = Text(page,'login-page-wrong-email-or-password-alert','Wrong email or password')

    @allure.step("Fill login form")
    def fill(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)

    @allure.step("Check visible login form")
    def check_visible(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")


