from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@mail.com1")

    # Заполняем поле Username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("007")

    # Заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("321654")

    # Нажимаем кнопку Registration
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Проверка, что на странице "Dashboard" отображается заголовок "Dashboard"
    dashboard_visible = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_visible).to_be_visible()
    expect(dashboard_visible).to_have_text('Dashboard')
