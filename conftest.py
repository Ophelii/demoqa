import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()


#   полезные декораторы:

#   @pytest.mark - для маркировки текста
#   @pytest.mark.skip - пропуск теста. он может иметь атрибуты, но может и не иметь. pytest.skip - можно ставить в середину
#   @pytest.mark.skipif(True, reason) - пропустит тест если условие - тру. есть обязательные параметры - True(булевая причина) и reason. если булевая - то второй аргумент обязательный, если нет - необязательный, но лучше писать два.
#   @pytest.mark.parametrize()