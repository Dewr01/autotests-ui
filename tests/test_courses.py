from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()  # Создание страницы

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

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка, что на странице "Course" отображается заголовок "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        # Проверка, что на странице "Course" отображается текст блока "There is no results"
        icon_view = page.get_by_test_id('courses-list-empty-view-icon')  # Иконка
        expect(icon_view).to_be_visible()

        title_text = page.get_by_test_id('courses-list-empty-view-title-text')  # Заголовок
        expect(title_text).to_be_visible()
        expect(title_text).to_have_text('There is no results')

        description_text = page.get_by_test_id('courses-list-empty-view-description-text')  # Текст блока
        expect(description_text).to_be_visible()
        expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
