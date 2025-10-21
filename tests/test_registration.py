from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):

        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        reg_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        reg_email_input.fill('user.name@gmail.com')

        reg_username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        reg_username_input.fill('username')

        reg_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        reg_password_input.fill('password')

        reg_registration_btn = chromium_page.get_by_test_id('registration-page-registration-button')
        reg_registration_btn.click()

        dashboard_title= chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()

        # dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
        # expect(dashboard).to_be_visible()


