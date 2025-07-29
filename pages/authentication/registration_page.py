from playwright.sync_api import Page

from config import settings
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from tools.routes import AppRoute


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)

    def navigate(self):
        self.page.goto(AppRoute.REGISTRATION)

    def fill_registration_form(self):
        self.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )

    def click_registration_button(self):
        self.registration_form.click_registration_button()

    def check_visible_registration_form(self):
        self.registration_form.check_visible(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
