import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        with allure.step(f'Открыть страницу {url}'):
            self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_if_visible(self, locator):
        buttons = self.driver.find_elements(*locator)
        if buttons and buttons[0].is_displayed():
            buttons[0].click()

    def click_via_javascript(self, locator):
        target = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].click();', target)

    def click_and_switch_to_new_window(self, locator):
        old_windows = set(self.driver.window_handles)
        self.click(locator)
        self.wait.until(EC.new_window_is_opened(old_windows))
        new_window = (set(self.driver.window_handles) - old_windows).pop()
        self.driver.switch_to.window(new_window)

    def enter_text(self, locator, text):
        input_field = self.find_element(locator)
        input_field.clear()
        input_field.send_keys(text)

    def press_enter(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    def get_text(self, locator):
        return self.find_element(locator).text

    def scroll_to_element(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});',
            target
        )

    def current_url_is(self, expected_url):
        try:
            self.wait.until(EC.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False

    def current_url_contains(self, url_part):
        try:
            self.wait.until(EC.url_contains(url_part))
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
