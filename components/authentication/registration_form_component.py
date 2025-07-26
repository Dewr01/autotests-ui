from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button
from elements.link import Link


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration Button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login Link')

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()
