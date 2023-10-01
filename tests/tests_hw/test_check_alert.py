import time
from conftest import browser
from pages.alerts import Alerts


def test_timer_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.timer_alert_btn.exist()
    alert_page.timer_alert_btn.click()
    assert not alert_page.alert()
    time.sleep(6)
    assert alert_page.alert()
    alert_page.alert().accept()