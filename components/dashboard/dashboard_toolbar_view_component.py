import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.dashboard_title = Text(page, "dashboard-toolbar-title-text", "Dashboard Title")

    @allure.step('Check visible Dashboard panel')
    def check_visible(self) -> None:
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text("Dashboard")
