from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка Registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@mail.com1")

    # Заполняем поле Username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("007")

    # Заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("321654")

    # Проверяем, что кнопка Registration активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).not_to_be_disabled()
