from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    reg_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    reg_email_input.fill('user.name@gmail.com')

    reg_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    reg_username_input.fill('username')

    reg_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    reg_password_input.fill('password')

    reg_registration_btn = page.get_by_test_id('registration-page-registration-button')
    reg_registration_btn.click()

    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()
