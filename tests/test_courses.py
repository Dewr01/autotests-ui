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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page, courses_list_page):
    # Шаг 1: Открыть страницу
    create_course_page.open()

    # Шаг 2 - 3: Проверить заголовок и состояние кнопки создания
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()

    # Шаг 4 - 5: Проверить блоки изображений
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()

    # Шаг 6: Проверить форму по умолчанию
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    # Шаг 7 - 9: Проверить раздел упражнений
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # Шаг 10 - 11: Загрузить изображение и проверить состояние загрузки
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.check_visible_preview_image()

    # Шаг 12: Заполнить форму курса
    course_data = {
        "title": "Playwright",
        "estimated_time": "2 weeks",
        "description": "Playwright",
        "max_score": "100",
        "min_score": "10"
    }
    create_course_page.fill_create_course_form(**course_data)

    # Шаг 13: Создать курс
    create_course_page.click_create_course_button()

    # Шаг 14 - 15: Проверить страницу списка курсов
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()

    # Шаг 16: Проверить карточку созданного курса
    courses_list_page.check_visible_course_card(
        index=0,
        title=course_data["title"],
        max_score=course_data["max_score"],
        min_score=course_data["min_score"],
        estimated_time=course_data["estimated_time"]
    )
