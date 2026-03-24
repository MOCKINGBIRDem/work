

from faker import Faker
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


faker = Faker()
class TestRadioButton():

    def test_radio_button(self, page: Page):
        page.goto("https://demoqa.com/radio-button")
        page.locator('//*[@id="yesRadio"]').click()
        expect(page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/p/span')).to_contain_text('Yes')
        page.locator('//*[@id="impressiveRadio"]').click()
        expect(page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/p/span')).to_contain_text('Impressive')
        expect(page.locator('//*[@id="noRadio"]')).to_be_disabled()


