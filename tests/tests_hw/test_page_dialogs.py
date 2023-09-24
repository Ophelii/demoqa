from conftest import browser
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.submenu_btns.check_count_elements(5)
