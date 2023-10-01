from conftest import browser
from pages.webtables import WebTables
import time


def testr_sort(browser):
    webtables_page = WebTables(browser)

    webtables_page.visit()
    headers = webtables_page.column_headers.find_elements()
    for header in headers:
        assert '-sort-asc' not in header.get_dom_attribute('class')
        header.click()
        time.sleep(1)
        assert '-sort-asc' in header.get_dom_attribute('class')
        time.sleep(1)
