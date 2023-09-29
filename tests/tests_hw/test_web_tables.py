from conftest import browser
from pages.webtables import WebTables
import time


def test_web_tables_elements(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.add_btn.exist()
    assert web_tables.row_4.get_dom_attribute('class') == 'rt-tr -padRow -even'
    web_tables.add_btn.click()
    assert web_tables.reg_form.visible()
    time.sleep(2)
    assert not web_tables.reg_form.get_dom_attribute('class') == 'was-validated'
    web_tables.submit_btn.click()
    time.sleep(2)
    assert web_tables.reg_form.get_dom_attribute('class') == 'was-validated'
    web_tables.first_name_field.send_keys('Olga')
    web_tables.last_name_field.send_keys('Petrovna')
    web_tables.email_field.send_keys('petrovna88@ttt.tt')
    web_tables.age_field.send_keys('37')
    web_tables.salary_field.send_keys('8000')
    web_tables.department_field.send_keys('accounting')
    web_tables.submit_btn.click()
    time.sleep(2)
    assert not web_tables.reg_form.exist()
    assert not web_tables.row_4.get_dom_attribute('class') == 'rt-tr -padRow -even'
    assert web_tables.row_4.get_dom_attribute('class') == 'rt-tr -even'
    assert web_tables.row_4_name.get_text() == 'Olga'
    assert 'Olga' and 'Petrovna' and 'petrovna88@ttt.tt' and '37' and '8000' and 'accounting' in web_tables.row_4.get_text()
    web_tables.edit_btn_4.click()
    time.sleep(2)
    assert web_tables.reg_form.visible()
    assert web_tables.first_name_field.get_dom_attribute('value') == 'Olga'
    web_tables.first_name_field.clear()
    web_tables.first_name_field.send_keys('Svetlana')
    web_tables.submit_btn.click()
    assert not web_tables.row_4_name.get_text() == 'Olga'
    assert web_tables.row_4_name.get_text() == 'Svetlana'
    web_tables.delete_btn_4.click()
    time.sleep(2)
    assert 'Svetlana' and 'Petrovna' and 'petrovna88@ttt.tt' and '37' and '8000' and 'accounting' not in web_tables.row_4.get_text()
    assert not web_tables.row_4.get_dom_attribute('class') == 'rt-tr -even'
    assert web_tables.row_4.get_dom_attribute('class') == 'rt-tr -padRow -even'

