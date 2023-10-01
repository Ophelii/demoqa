from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElement:
    def __init__(self, driver, locator=None, locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + " not correct")
        return False


    def check_count_elements(self, count:int) -> bool:
        # return len(self.find_elements()) == count:     -  одна строка аналогична по действию трем строкам с if
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def scroll_to_element(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element())
        # можно альтернативно использовать "window.scrollTo(0, document.body.scrollHeight);" как первый аргумент

    def get_dom_attribute(self, name:str):
        value = self.find_element().get_dom_attribute(name)
        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def check_attribute_value(self, name, expected_value:str):
        actual_value = self.get_dom_attribute(name)
        if actual_value == expected_value:
            return True
        return False

        return check_attribute

    # def wait_untill(self, name:str, value=''):
    #     return WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.find_element().get_dom_attribute() == value))




        #
        # from selenium.webdriver import ActionChains
        # action_chains = ActionChains(browser)
        # action_chains.drag_and_drop(element, target).perform()
        #