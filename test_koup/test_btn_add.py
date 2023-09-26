from conftest import browser
from pages.herokuapp import HerokuApp
from pages.herkuapp_add_remove import AddRemove

def test_btn_add(browser):
    herokuapp = HerokuApp(browser)
    herokuapp_add_remove = AddRemove(browser)

    herokuapp.visit()
    assert herokuapp.equal_url()
    assert herokuapp.add_remove.get_text() == "Add/Remove Elements"
    herokuapp.add_remove.click()
    assert herokuapp_add_remove.equal_url()
    assert herokuapp_add_remove.add_element_btn.get_text() == 'Add Element'
    assert herokuapp_add_remove.add_element_btn.get_dom_attribute('onclick') == "addElement()"
    for i in range(4):
        herokuapp_add_remove.add_element_btn.click()
    assert herokuapp_add_remove.delete_btns.check_count_elements(4)
    for element in herokuapp_add_remove.delete_btns.find_elements():
        assert element.text == 'Delete'
    while herokuapp_add_remove.delete_btns.exist():
        herokuapp_add_remove.delete_btns.click()
    assert not herokuapp_add_remove.delete_btns.exist()
