from conftest import browser
# from pages.elements_page import ElementsPage
from pages.checkbox import CheckBox


# def test_find_elements(browser):
#     elements_page = ElementsPage(browser)

#     elements_page.visit()
#     assert elements_page.btns_first_menu.check_count_elements(9)

def test_count_checkbox(browser):
    checkbox = CheckBox(browser)

    checkbox.visit()
    assert checkbox.check_box.check_count_elements(1)
    checkbox.plus_btn.click()
    assert checkbox.check_box.check_count_elements(17)
    browser.refresh()
    assert checkbox.check_box.check_count_elements(1)
