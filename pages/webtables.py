from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.locator = None
        self.base_url = 'https://demoqa.com/webtables/'
        super().__init__(driver, self.base_url)

        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.reg_form = WebElement(driver, '#userForm')
        self.submit_btn = WebElement(driver, '#submit')
        self.first_name_field = WebElement(driver, '#firstName')
        self.last_name_field = WebElement(driver, '#lastName')
        self.email_field = WebElement(driver, '#userEmail')
        self.age_field = WebElement(driver, '#age')
        self.salary_field = WebElement(driver, '#salary')
        self.department_field = WebElement(driver, '#department')
        self.row_list = WebElement(driver, 'div.rt-tbody > div')
        self.row_4 = WebElement(driver, '.rt-tbody > div:nth-child(4) > div')
        self.row_4_name = WebElement(driver, ' div:nth-child(4) > div > div:nth-child(1)')
        self.edit_btn_4 = WebElement(driver, '#edit-record-4')
        self.delete_btn_4 = WebElement(driver,'#delete-record-4')
