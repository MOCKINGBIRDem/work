
class TestWebTable:
    def test_web_table(self, web_table):
        web_table.web_tables_check()
        web_table.edit_email()
        web_table.delete()
        web_table.search()