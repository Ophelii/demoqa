from conftest import browser
from pages.demoqa import DemoQA


def test_icon_exist(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_icon()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()









# from conftest import browser
# from pages.demoqa import DemoQA


# def test_icon_demoqa(browser):
#     browser.get("https://demoqa.com/")
#     icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
#
#     if icon is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')
