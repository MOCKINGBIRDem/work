from time import sleep

from faker import Faker
from playwright.sync_api import Page, expect


faker = Faker()
class TestWebTables():


    def test_web_tables(self, page: Page):
        page.goto("https://demoqa.com/webtables")
        i=0
        while i < 20:
            i+=1
            page.locator('//*[@id="addNewRecordButton"]').click()
            first_name = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
            page.get_by_placeholder("First Name").fill(first_name)
            last_name = f"{faker.last_name()}{faker.random_int(1000, 9999)}"
            page.get_by_placeholder("Last Name").fill(last_name)
            email = faker.email()
            page.get_by_placeholder("name@example.com").fill(email)
            age = f"{faker.random_int()}"
            page.get_by_placeholder("Age").fill(age)
            salary = f"{faker.random_int()}"
            page.get_by_placeholder("Salary").fill(salary)
            department = f"{faker.first_name()}{faker.random_int(1000, 9999)}"
            page.get_by_placeholder("Department").fill(department)
            page.locator('//*[@id="submit"]').click()
        page.select_option('//select', value="20")
        expect(page.locator(f'//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[1]')).to_be_visible()
        page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/button[3]').click()
        expect(page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/strong')).to_have_text("2 of 2")




    def test_edit_email(self, page: Page):
        email = faker.email()
        page.goto("https://demoqa.com/webtables")
        page.locator('//*[@id="edit-record-1"]').click()
        page.get_by_placeholder("name@example.com").clear()
        page.get_by_placeholder("name@example.com").fill(email)
        page.locator('//*[@id="submit"]').click()
        expect(page.locator(f"tr:has text({email})"))

    def test_delete(self, page: Page):
        page.goto("https://demoqa.com/webtables")
        page.locator('//*[@id="delete-record-1"]').click()
        expect(page.locator('//*[@id="delete-record-1"]')).to_have_count(0)

    def test_search(self, page: Page):
        page.goto("https://demoqa.com/webtables")
        page.get_by_placeholder('Type to search').fill("Kierra")
        expect(page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]')).to_be_visible()





