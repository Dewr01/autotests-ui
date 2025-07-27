from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)

    def navigate(self):
        self.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_form.fill(email=email, username=username, password=password)

    def click_registration_button(self):
        self.registration_form.click_registration_button()

    def check_visible_registration_form(self, email: str = "", username: str = "", password: str = ""):
        self.registration_form.check_visible(email=email, username=username, password=password)
