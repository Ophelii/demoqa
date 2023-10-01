import time
from conftest import browser
from pages.webtables import WebTables


def test_webtables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    # assert web_tables.row_1.get_dom_attribute('class') == 'rt-tr -odd'
    assert not web_tables.no_rowds.exist()

    while web_tables.all_delete_btns.exist():
        web_tables.all_delete_btns.click()

    time.sleep(2)

    # assert not web_tables.row_1.get_dom_attribute('class') == 'rt-tr -odd'
    # assert web_tables.row_1.get_dom_attribute('class') == 'rt-tr -padRow -odd'
    assert web_tables.no_rowds.exist()
