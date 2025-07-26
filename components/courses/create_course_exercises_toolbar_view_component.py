from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title_exercises = Text(page, "create-course-exercises-box-toolbar-title-text", "Exercises Title")
        self.create_exercise_button = Button(
            page, "create-course-exercises-box-toolbar-create-exercise-button", "Create Exercise Button"
        )

    def check_visible(self) -> None:
        self.title_exercises.check_visible()
        self.title_exercises.check_have_text("Exercises")
        self.create_exercise_button.check_visible()
        self.create_exercise_button.check_enabled()

    def click_create_exercise_button(self) -> None:
        self.create_exercise_button.click()
