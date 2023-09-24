from conftest import browser
from pages.textbox import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    name_text = 'Nickolai Tester'
    address_text = 'Somewhere east'

    text_box.visit()
    text_box.full_name.send_keys(name_text)
    text_box.current_address.send_keys(address_text)
    text_box.submit_btn.click()

    assert text_box.output_box.visible()
    assert name_text and address_text in text_box.output_box.get_text()