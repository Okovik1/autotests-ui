import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright)->Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()

@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        reg_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        reg_email_input.fill('user.name@gmail.com')

        reg_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        reg_username_input.fill('username')

        reg_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        reg_password_input.fill('password')

        reg_registration_btn = page.get_by_test_id('registration-page-registration-button')
        reg_registration_btn.click()

        context.storage_state(path='browser-state.json')

@pytest.fixture(scope="function")
def chromium_page_with_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()
        yield page
