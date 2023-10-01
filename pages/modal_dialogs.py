from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.locator = None
        self.base_url = 'https://demoqa.com/modal-dialogs/'
        super().__init__(driver, self.base_url)

        self.submenu_btns = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.main_page_icon = WebElement(driver, '#app > header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.modal_large_close_btn = WebElement(driver, '#closeLargeModal')
        self.modal_small_close_btn = WebElement(driver, '#closeSmallModal')
        self.modal_close_btns = WebElement(driver, '/html/body/div[4]/div/div/div[3]/button', 'xpath')


