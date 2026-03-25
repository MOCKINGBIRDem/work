from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from base_test import BaseTest


class TextboxPage(BaseTest):

    def __init__(self, page: Page):
        super().__init__(page)

    def text_box_check(self):
        name = self.fake_name()
        email = self.fake_email()
        current_address = self.fake_current_address()
        permanent_address = self.fake_permanent_address()
        self.navigate("text-box")
        self.page.get_by_placeholder("Full Name").fill(name)
        self.page.get_by_placeholder("name@example.com").fill(email)
        self.page.get_by_placeholder("Current Address").fill(current_address)
        self.page.locator('//*[@id="permanentAddress"]').fill(permanent_address)
        self.page.locator('//*[@id="submit"]').click()
        expect(self.page.locator('#name')).to_contain_text(name)
        expect(self.page.locator('//*[@id="email"]')).to_contain_text(email)
        expect(self.page.locator('p#currentAddress')).to_contain_text(current_address)
        expect(self.page.locator('p#permanentAddress')).to_contain_text(permanent_address)


