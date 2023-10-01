from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button/'

        super().__init__(driver, self.base_url)

        self.yes_btn = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(2) > label')
        self.impressive_btn = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3) > label')
        self.massage_text = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p')
        self.no_btn = WebElement(driver, '.disabled.custom-radio')