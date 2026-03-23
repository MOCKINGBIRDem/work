from time import sleep

from faker import Faker
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from base_test import BaseTest

faker = Faker()
class TestBase():

    def test_text_box(self, page: Page):
        page.goto("https://demoqa.com/text-box")
        name = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        email = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        current_address = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        permanent_address = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        page.get_by_placeholder("Full Name").fill(name)
        page.get_by_placeholder("name@example.com").fill(email + "@mail.ru")
        page.get_by_placeholder("Current Address").fill(current_address)
        page.locator('//*[@id="permanentAddress"]').fill(permanent_address)
        page.locator('//*[@id="submit"]').click()
        expect(page.locator('#name')).to_contain_text(name)
        expect(page.locator('//*[@id="email"]')).to_contain_text(email + "@mail.ru")
        expect(page.locator('p#currentAddress')).to_contain_text(current_address)
        expect(page.locator('p#permanentAddress')).to_contain_text(permanent_address)

