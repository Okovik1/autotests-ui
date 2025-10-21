import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

# @pytest.fixture
# def chromium_page():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         yield browser.new_page()

@pytest.fixture
def chromium_page(playwright: Playwright)->Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()