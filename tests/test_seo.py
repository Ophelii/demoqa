import time
import pytest
from conftest import browser
from pages.demoqa import DemoQA
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.textbox import TextBox


# def test_seo(browser):
#     demo_qa_page = DemoQA(browser)
#
#     demo_qa_page.visit()
#     assert demo_qa_page.get_title() == 'DEMOQA'   # или assert browser.ti


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQA, BrowserTab, TextBox])
def test_check_title_all_pages(browser, pages):
        page = pages(browser)

        page.visit()
        time.sleep(2)
        assert page.get_title() == 'DEMOQA'