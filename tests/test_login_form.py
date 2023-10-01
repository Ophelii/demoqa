from conftest import browser
import time
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('testers@tt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.user_hobbies.scroll_to_element()
    form_page.user_hobbies.click()
    form_page.current_address.send_keys('Spb')

    form_page.user_state.click()
    time.sleep(2)
    form_page.state_select.click()
    time.sleep(2)
    form_page.user_city.click()
    time.sleep(2)
    form_page.city_select.click()
    time.sleep(2)

    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.visible()
    form_page.btn_close_modal.click_force()
