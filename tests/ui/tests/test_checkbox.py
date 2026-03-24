

from faker import Faker
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page



faker = Faker()
class TestCheckbox():

    def test_checkbox(self, page: Page):
        page.goto("https://demoqa.com/checkbox")
        page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div/span[2]').click()
        page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/span[3]').click()
        page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[4]/span[3]').click()
        expect(page.locator('//*[@id="result"]/span[2]')).to_contain_text('desktop')
        expect(page.locator('//*[@id="result"]/span[3]')).to_contain_text('notes')
        expect(page.locator('//*[@id="result"]/span[4]')).to_contain_text('commands')
        expect(page.locator('//*[@id="result"]/span[5]')).to_contain_text('downloads')
        expect(page.locator('//*[@id="result"]/span[6]')).to_contain_text('wordFile')
        expect(page.locator('//*[@id="result"]/span[7]')).to_contain_text('excelFile')




