from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.column = None
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
        self.delete_btn_1 = WebElement(driver,'#delete-record-1')
        self.delete_btn_2 = WebElement(driver, '#delete-record-2')
        self.delete_btn_3 = WebElement(driver, '#delete-record-3')
        self.no_rowds = WebElement(driver, 'div.rt-noData')
        self.row_1 = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div')
        self.select_page_row = WebElement(driver, '.-pageSizeOptions > select')
        self.select_5_row = WebElement(driver, 'select > option:nth-child(1)')
        self.select_10_row = WebElement(driver, 'select > option:nth-child(2)')
        self.previous_btn = WebElement(driver, ' div.-previous > button')
        self.next_btn = WebElement(driver, 'div.-next > button')
        self.span_page_info = WebElement(driver, 'span.-pageInfo')
        self.page_info = WebElement(driver, 'span.-pageInfo')
        self.page_input = WebElement(driver, 'input[type=number]')
        self.all_delete_btns = WebElement(driver, '//*[@title="Delete"]', 'xpath')
        self.column_headers = WebElement(driver, 'div.rt-th.rt-resizable-header')
        self.column_1 = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.column_2 = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(2)')
        self.column_3 = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(3)')
        self.column_4 = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(4)')
        self.column_5 = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(5)')
        self.column_6 = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(6)')
