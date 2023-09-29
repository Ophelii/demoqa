import time
import pytest
from conftest import browser
from pages.demoqa import DemoQA
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQA, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.view_port.exist()
    assert page.view_port.get_dom_attribute('name') == 'viewport'
    assert page.view_port.get_dom_attribute('content') == 'width=device-width,initial-scale=1'


