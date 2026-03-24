from time import sleep

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page



class TestLinks():

    def test_links(self, page: Page):
        page.goto("https://demoqa.com/links")
        with page.context.expect_page() as new_page_info:
            page.locator('//*[@id="simpleLink"]').click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://demoqa.com/")

    def test_links2(self, page: Page):
        page.goto("https://demoqa.com/links")
        with page.context.expect_page() as new_page_info:
            page.locator('//*[@id="dynamicLink"]').click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://demoqa.com/")

