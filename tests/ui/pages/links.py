from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from base_test import BaseTest


class LinksPage(BaseTest):

    def __init__(self, page: Page):
        super().__init__(page)

    def links_check(self):
        self.navigate("links")
        with self.page.context.expect_page() as new_page_info:
            self.page.locator('//*[@id="simpleLink"]').click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://demoqa.com/")

    def links_check2(self):
        self.navigate("links")
        with self.page.context.expect_page() as new_page_info:
            self.page.locator('//*[@id="dynamicLink"]').click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://demoqa.com/")

