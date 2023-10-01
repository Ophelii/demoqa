from selenium.webdriver.common.by import By
from conftest import browser
import time
from pages.progress_bar import ProgressBar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_progress_bar(browser):
    progress_page = ProgressBar(browser)
    wait = WebDriverWait(browser, 60)
    progress_page.visit()

    time.sleep(2)
    progress_page.start_stop_btn.click()

    wait.until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, '#progressBar > div'), "aria-valuenow", "51"))
    progress_page.start_stop_btn.click()

    time.sleep(2)
    assert progress_page.current_progress.get_dom_attribute("aria-valuenow") == '51'



