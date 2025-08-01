import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, 'create-course-toolbar-title-text', 'Create Course Title')
        self.create_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course Button')

    @allure.step('Check visible course creation panel')
    def check_visible(self, is_create_course_disabled: bool = True) -> None:
        self.title.check_visible()
        self.title.check_have_text('Create course')
        self.create_button.check_visible()
        if is_create_course_disabled:
            self.create_button.check_disabled()
        else:
            self.create_button.check_enabled()

    def click_create_course_button(self):
        self.create_button.click()
