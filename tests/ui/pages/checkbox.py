from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from base_test import BaseTest


class CheckboxPage(BaseTest):

    def __init__(self, page: Page):
        super().__init__(page)

    def checkbox_check(self):
        self.navigate("checkbox")
        self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/span[2]').click()
        self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/span[3]').click()
        self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[4]/span[3]').click()
        expect(self.page.locator('//*[@id="result"]/span[2]')).to_contain_text('desktop')
        expect(self.page.locator('//*[@id="result"]/span[3]')).to_contain_text('notes')
        expect(self.page.locator('//*[@id="result"]/span[4]')).to_contain_text('commands')
        expect(self.page.locator('//*[@id="result"]/span[5]')).to_contain_text('downloads')
        expect(self.page.locator('//*[@id="result"]/span[6]')).to_contain_text('wordFile')
        expect(self.page.locator('//*[@id="result"]/span[7]')).to_contain_text('excelFile')




