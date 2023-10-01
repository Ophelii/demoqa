from conftest import browser
from pages.demoqa import DemoQA
from pages.radio_button import RadioButton
# import time
import pytest


@pytest.mark.skip
def test_decor_3(browser):
    demo_qa = DemoQA(browser)

    demo_qa.visit()
    assert demo_qa.h5_titles.check_count_elements(6)

    for element in demo_qa.h5_titles.find_elements():
        assert element.text != ''   # альтернативная запись: assert not element.text == ''



# @pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_1(browser):
    # pytest.skip()
    radio_btn = RadioButton(browser)

    if not radio_btn.code_status():
        return pytest.skip(reason=f'Страница {radio_btn.base_url} недоступна')

    # альтернативная запись действия выше(должно быть равно код 200,код 400 - взят для проверки)
    # if radio_btn.code_status() == 400:
    #     return pytest.skip(reason=f'Страница {radio_btn.base_url} недоступна')

    radio_btn.visit()
    radio_btn.yes_btn.click_force()

    assert radio_btn.massage_text.get_text() == 'You have selected Yes'

    radio_btn.impressive_btn.click_force()
    assert radio_btn.massage_text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio_btn.no_btn.get_dom_attribute('class')
