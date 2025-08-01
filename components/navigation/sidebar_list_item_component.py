from typing import Pattern
import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', f'{identifier} Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', f'{identifier} Title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', f'{identifier} Button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
