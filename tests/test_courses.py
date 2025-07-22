import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка, что на странице "Course" отображается заголовок "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверка, что на странице "Course" отображается текст блока "There is no results"
    # Иконка
    icon_view = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_view).to_be_visible()

    # Заголовок
    title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_text).to_be_visible()
    expect(title_text).to_have_text('There is no results')

    # Текст блока
    description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_be_visible()
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
