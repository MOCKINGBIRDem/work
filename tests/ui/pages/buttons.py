from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from base_test import BaseTest


class ButtonsPage(BaseTest):

    def __init__(self, page: Page):
        super().__init__(page)

    def button_check(self):
        self.navigate("buttons")
        self.page.locator('//*[@id="doubleClickBtn"]').dblclick()
        expect(self.page.locator('//*[@id="doubleClickMessage"]')).to_be_visible()
        self.page.locator('//*[@id="rightClickBtn"]').click(button='right')
        expect(self.page.locator('//*[@id="rightClickMessage"]')).to_be_visible()
        self.page.locator("//button[text()='Click Me']").click()
        expect(self.page.locator('//*[@id="dynamicClickMessage"]')).to_be_visible()

