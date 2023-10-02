from conftest import browser
import time
from pages.slider import Slider
from selenium.webdriver import ActionChains, Keys


def test_slider(browser):
    slider_page = Slider(browser)
    action_chains = ActionChains(browser)

    slider_page.visit()
    browser.maximize_window()
    assert slider_page.slider_value.exist()
    assert slider_page.slider_container.exist()
    assert slider_page.slider_container.get_dom_attribute('value') == '25'
    assert slider_page.slider_value.get_dom_attribute('value') == '25'
    # assert slider_page.slider_btn.get_dom_attribute('style') == 'left: calc(25% + 5px);'

    while slider_page.slider_container.get_dom_attribute('value') != '50':
        slider_page.slider_container.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_container.get_dom_attribute('value') == '50'
    assert slider_page.slider_value.get_dom_attribute('value') == '50'
    # assert slider_page.slider_btn.get_dom_attribute('style') == 'left: calc(50% + 0px);'

    time.sleep(2)


