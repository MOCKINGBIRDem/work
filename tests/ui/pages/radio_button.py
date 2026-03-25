from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page
from base_test import BaseTest

class RadioButtonPage(BaseTest):

    def __init__(self, page: Page):
        super().__init__(page)

    def radio_button_check(self):
        self.navigate("radio-button")
        self.page.locator('//*[@id="yesRadio"]').click()
        expect(self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/p/span')).to_contain_text('Yes')
        self.page.locator('//*[@id="impressiveRadio"]').click()
        expect(self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/p/span')).to_contain_text('Impressive')
        expect(self.page.locator('//*[@id="noRadio"]')).to_be_disabled()


