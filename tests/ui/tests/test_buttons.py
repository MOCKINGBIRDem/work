from time import sleep

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page



class TestButtons():

    def test_radio_button(self, page: Page):
        page.goto("https://demoqa.com/buttons")
        page.locator('//*[@id="doubleClickBtn"]').dblclick()
        expect(page.locator('//*[@id="doubleClickMessage"]')).to_be_visible()
        page.locator('//*[@id="rightClickBtn"]').click(button='right')
        expect(page.locator('//*[@id="rightClickMessage"]')).to_be_visible()
        page.locator("//button[text()='Click Me']").click()
        expect(page.locator('//*[@id="dynamicClickMessage"]')).to_be_visible()

