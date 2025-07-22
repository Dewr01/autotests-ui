import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("username@gmail.com", "tester", "password")
    ]
)
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email: str,
        username: str,
        password: str
):

    registration_page.navigate()
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_page.should_be_dashboard_page()
