import time
from conftest import browser
from pages.webtables import WebTables


def test_next_previous(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.select_page_row.scroll_to_element()
    assert web_tables.row_list.check_count_elements(10)
    web_tables.select_page_row.click()
    time.sleep(2)
    web_tables.select_5_row.click()
    time.sleep(2)

    assert not web_tables.row_list.check_count_elements(10)
    assert web_tables.row_list.check_count_elements(5)
    assert web_tables.previous_btn.get_dom_attribute('disabled')
    assert web_tables.next_btn.get_dom_attribute('disabled')
    assert web_tables.page_info.get_text() == 'Page of 1'

    for i in range(3):
        web_tables.add_btn.click()
        time.sleep(2)
        web_tables.first_name_field.send_keys('Olga')
        web_tables.last_name_field.send_keys('Petrovna')
        web_tables.email_field.send_keys('petrovna88@ttt.tt')
        web_tables.age_field.send_keys('37')
        web_tables.salary_field.send_keys('8000')
        web_tables.department_field.send_keys('accounting')
        web_tables.submit_btn.click()
        time.sleep(2)

    assert web_tables.page_info.get_text() == 'Page of 2'
    assert not web_tables.next_btn.get_dom_attribute('disabled')
    web_tables.next_btn.click()
    time.sleep(2)

    assert web_tables.page_input.get_dom_attribute('value') == '2'
    assert not web_tables.previous_btn.get_dom_attribute('disabled')
    web_tables.previous_btn.click()
    time.sleep(2)
    assert web_tables.page_input.get_dom_attribute('value') == '1'



