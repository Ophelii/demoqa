from pages.base_page import BasePage
from components.components import WebElement


class AddRemove(BasePage):
    def __init__(self, driver):
        self.locator = None
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.add_element_btn = WebElement(driver, '#content > div > button')
        self.delete_btns = WebElement(driver, '#elements > button')
        self.delete_btn_1 = WebElement(driver, '#elements > button:nth-child(1)')
        self.delete_btn_2 = WebElement(driver, '#elements > button:nth-child(2)')
        self.delete_btn_3 = WebElement(driver, '#elements > button:nth-child(3)')
        self.delete_btn_4 = WebElement(driver, '#elements > button:nth-child(4)')

