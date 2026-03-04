from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page,'registration-form-email-input', "Registration email input")
        self.username_input = Input(page,'registration-form-username-input','Registration username input')
        self.password_input = Input(page,'registration-form-password-input','Registration password input')
        self.registration_btn = Button(page,'registration-page-registration-button', 'Registration button')

    def fill(self, email, username, password):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def check_visible(self,email,username,password):
        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password)
