import os

import allure
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    if os.getenv('HEADLESS') == '1':
        firefox_options.add_argument('-headless')
    firefox_driver = webdriver.Firefox(options=firefox_options)
    firefox_driver.set_window_size(1440, 1000)
    yield firefox_driver
    if firefox_driver.session_id:
        allure.attach(
            firefox_driver.get_screenshot_as_png(),
            name='Последнее состояние страницы',
            attachment_type=allure.attachment_type.PNG
        )
    firefox_driver.quit()
