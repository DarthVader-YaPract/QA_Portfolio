import allure
from selenium.common.exceptions import TimeoutException

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Принять cookies, если баннер показан")
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    @allure.step("Открыть ответ на вопрос с индексом {index}")
    def get_faq_answer(self, index):
        question = MainPageLocators.faq_question(index)
        self.scroll_to(question)
        self.click(question)
        return self.get_text(MainPageLocators.faq_answer(index))

    @allure.step("Нажать верхнюю кнопку «Заказать»")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку «Заказать»")
    def click_bottom_order_button(self):
        self.scroll_to(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        old_windows = self.driver.window_handles
        self.click(MainPageLocators.YANDEX_LOGO)
        self.wait.until(lambda driver: len(driver.window_handles) > len(old_windows))
        new_window = next(window for window in self.driver.window_handles if window not in old_windows)
        self.driver.switch_to.window(new_window)

    @allure.step("Проверить статус несуществующего заказа {number}")
    def search_order(self, number):
        self.type_text(MainPageLocators.ORDER_NUMBER_INPUT, number)
        self.click(MainPageLocators.ORDER_STATUS_BUTTON)

