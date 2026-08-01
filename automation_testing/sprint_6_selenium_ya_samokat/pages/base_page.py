import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).is_displayed()

    def scroll_to(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_for_url(self, url_part):
        return self.wait.until(ec.url_contains(url_part))

