from conftest import browser
from pages.elements_page import ElementsPage
from pages.demoqa import DemoQA


def test_navigation(browser):
    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    elements_page.refresh()
    demo_qa_page.refresh()
    demo_qa_page.back()
    demo_qa_page.forward()
    assert elements_page.equal_url()

