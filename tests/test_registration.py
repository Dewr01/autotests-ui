import pytest
from playwright.sync_api import expect

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):

    registration_page.navigate()
    registration_page.fill_registration_form(email="username@gmail.com", username="tester", password="password")
    registration_page.click_registration_button()

    expect(dashboard_page.page).to_have_url(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
    )
    dashboard_page.check_visible_dashboard_title()
