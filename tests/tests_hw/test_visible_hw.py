from conftest import browser
from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.section1_content.visible()
    accordion_page.section_heading.click()
    time.sleep(2)
    assert not accordion_page.section1_content.visible()


def test_visible_accordion_default(browser):
    accordion_page2 = Accordion(browser)

    accordion_page2.visit()
    assert accordion_page2.view_port.exist()
    # assert not accordion_page2.section2_content1.visible()
    # assert not accordion_page2.section2_content2.visible()
    # assert not accordion_page2.section3_content.visible()

