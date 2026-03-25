from time import sleep

from playwright.sync_api import Page, expect

from base_test import BaseTest

class WebTablePage(BaseTest):

    def __init__(self, page: Page):
        super().__init__(page)


    def web_tables_check(self):
        self.navigate("webtables")
        i=0
        while i < 20:
            i+=1
            self.page.locator('//*[@id="addNewRecordButton"]').click()
            self.page.get_by_placeholder("First Name").fill(self.fake_first_name())
            self.page.get_by_placeholder("Last Name").fill(self.fake_last_name())
            self.page.get_by_placeholder("name@example.com").fill(self.fake_email())
            self.page.get_by_placeholder("Age").fill(self.fake_age())
            self.page.get_by_placeholder("Salary").fill(self.fake_salary())
            self.page.get_by_placeholder("Department").fill(self.fake_department())
            self.page.locator('//*[@id="submit"]').click()
        self.page.select_option('//select', value="20")
        expect(self.page.locator(f'//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[1]')).to_be_visible()
        self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/button[3]').click()
        expect(self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/strong')).to_have_text("2 of 2")




    def edit_email(self):
        self.navigate("webtables")
        self.page.locator('//*[@id="edit-record-1"]').click()
        self.page.get_by_placeholder("name@example.com").clear()
        self.page.get_by_placeholder("name@example.com").fill(self.fake_email())
        self.page.locator('//*[@id="submit"]').click()
        expect(self.page.locator(f"tr:has text({self.fake_email()})"))

    def delete(self):
        self.navigate("webtables")
        self.page.locator('//*[@id="delete-record-1"]').click()
        expect(self.page.locator('//*[@id="delete-record-1"]')).to_have_count(0)

    def search(self):
        self.navigate("webtables")
        self.page.get_by_placeholder('Type to search').fill("Kierra")
        expect(self.page.locator('//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]')).to_be_visible()





