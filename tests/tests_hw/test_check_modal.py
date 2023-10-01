from conftest import browser
from pages.modal_dialogs import ModalDialogs
import time
import pytest


# @pytest.mark.skipif(True, reason='просто пропуск')
def test_check_modal(browser):
    modal_page = ModalDialogs(browser)

    modal_page.visit()

    if not modal_page.code_status():
        pytest.skip(reason=f'Страница {modal_page.base_url} недоступна')

    assert modal_page.small_modal.exist()
    assert modal_page.large_modal.exist()
    assert not modal_page.modal_dialog.exist()

    modal_page.small_modal.click()
    time.sleep(1)

    assert modal_page.modal_dialog.visible()
    assert modal_page.modal_close_btns.visible()
    modal_page.modal_close_btns.click()

    assert not modal_page.modal_dialog.exist()
    modal_page.large_modal.click()
    time.sleep(1)

    assert modal_page.modal_dialog.visible()
    assert modal_page.modal_close_btns.visible()
    modal_page.modal_close_btns.click()

    assert not modal_page.modal_dialog.exist()
