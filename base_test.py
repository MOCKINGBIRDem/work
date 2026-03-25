from faker import Faker
from playwright.sync_api import Page
faker = Faker()


class BaseTest():
    def fake_email(self):
        email = faker.email()
        return email

    def fake_permanent_address(self):
        permanent_address = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        return permanent_address

    def fake_current_address(self):
        current_address = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        return current_address

    def fake_name(self):
        name = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        return name

    def fake_last_name(self):
        last_name = f"{faker.last_name()}{faker.random_int(1000, 9999)}"
        return last_name

    def fake_first_name(self):
        first_name = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        return first_name

    def fake_age(self):
        age = f"{faker.random_int()}"
        return age

    def fake_salary(self):
        salary = f"{faker.random_int()}"
        return salary

    def fake_department(self):
        department = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
        return department


    def __init__(self, page: Page):
        self.page = page

    def navigate(self, link: str):
        self.page.goto(f"https://demoqa.com/{link}")

