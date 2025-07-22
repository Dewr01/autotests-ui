import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Процесс регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@mail.com1")

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("007")

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("321654")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

        # Закрываем все ресурсы внутри фикстуры
        context.close()
        browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()

    context.close()
    browser.close()
