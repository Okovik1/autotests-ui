from pages.base_page import BasePage
from playwright.sync_api import Page,expect


class RegistrationPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

        self.reg_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.reg_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.reg_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.reg_registration_btn = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self,email,username, password):
        self.reg_email_input.fill(email)
        self.reg_username_input.fill(username)
        self.reg_password_input.fill(password)

        expect(self.reg_email_input).to_have_value(email)
        expect(self.reg_username_input).to_have_value(username)
        expect(self.reg_password_input).to_have_value(password)

    def click_registration_button(self):
        self.reg_registration_btn.click()
