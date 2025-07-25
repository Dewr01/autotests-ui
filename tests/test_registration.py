import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.navigate()
    registration_page.fill_registration_form(
        email="username@gmail.com",
        username="tester",
        password="password"
    )
    registration_page.click_registration_button()
    dashboard_page.dashboard_title.check_visible()
