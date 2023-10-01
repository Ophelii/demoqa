from conftest import browser
import time
from pages.slider import Slider
from selenium.webdriver import ActionChains


def test_slider(browser):
    slider_page = Slider(browser)
    action_chains = ActionChains(browser)

    slider_page.visit()

    assert slider_page.slider_value.exist()
    assert slider_page.slider_container.exist()
    assert slider_page.slider_container.get_dom_attribute('value') == '25'
    assert slider_page.slider_value.get_dom_attribute('value') == '25'
    # assert slider_page.slider_btn.get_dom_attribute('style') == 'left: calc(25% + 5px);'

    action_chains.drag_and_drop_by_offset(
        slider_page.slider_container.find_element(),
        2, 0
    ).perform()
    time.sleep(1)

    assert slider_page.slider_container.get_dom_attribute('value') == '50'
    assert slider_page.slider_value.get_dom_attribute('value') == '50'
    # assert slider_page.slider_btn.get_dom_attribute('style') == 'left: calc(50% + 0px);'

    time.sleep(2)
