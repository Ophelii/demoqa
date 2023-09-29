# import time
from conftest import browser
from pages.webtables import WebTables


def test_webtables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.row_1.get_dom_attribute('class') == 'rt-tr -odd'
    assert not web_tables.no_rowds.exist()
    while web_tables.delete_btn_1.exist() == True:
            web_tables.delete_btn_1.click()
    else:
            web_tables.delete_btn_1.exist()

    # web_tables.delete_btn_2.click()
    # web_tables.delete_btn_3.click()
    assert not web_tables.row_1.get_dom_attribute('class') == 'rt-tr -odd'
    assert web_tables.row_1.get_dom_attribute('class') == 'rt-tr -padRow -odd'
    assert web_tables.no_rowds.visible()