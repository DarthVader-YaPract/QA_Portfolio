import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    QUESTIONS = [
        MainPageLocators.IMPORTANT_QUESTION_0,
        MainPageLocators.IMPORTANT_QUESTION_1,
        MainPageLocators.IMPORTANT_QUESTION_2,
        MainPageLocators.IMPORTANT_QUESTION_3,
        MainPageLocators.IMPORTANT_QUESTION_4,
        MainPageLocators.IMPORTANT_QUESTION_5,
        MainPageLocators.IMPORTANT_QUESTION_6,
        MainPageLocators.IMPORTANT_QUESTION_7,
    ]
    ANSWERS = [
        MainPageLocators.IMPORTANT_ANSWER_0,
        MainPageLocators.IMPORTANT_ANSWER_1,
        MainPageLocators.IMPORTANT_ANSWER_2,
        MainPageLocators.IMPORTANT_ANSWER_3,
        MainPageLocators.IMPORTANT_ANSWER_4,
        MainPageLocators.IMPORTANT_ANSWER_5,
        MainPageLocators.IMPORTANT_ANSWER_6,
        MainPageLocators.IMPORTANT_ANSWER_7,
    ]

    @allure.step('Принять cookies, если баннер отображается')
    def accept_cookies(self):
        self.click_if_visible(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Открыть ответ на вопрос с индексом {index}')
    def get_important_answer(self, index):
        question = self.QUESTIONS[index]
        answer = self.ANSWERS[index]
        self.scroll_to_element(question)
        self.click_via_javascript(question)
        return self.get_text(answer)

    @allure.step('Начать заказ через верхнюю кнопку')
    def start_order_from_top(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Начать заказ через нижнюю кнопку')
    def start_order_from_lower_button(self):
        self.scroll_to_element(MainPageLocators.LOWER_ORDER_BUTTON)
        self.click(MainPageLocators.LOWER_ORDER_BUTTON)

    @allure.step('Начать заказ через выбранную кнопку')
    def start_order(self, order_button):
        self.scroll_to_element(order_button)
        self.click(order_button)

    @allure.step('Нажать логотип Самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажать логотип Яндекса и перейти в новое окно')
    def click_yandex_logo(self):
        self.click_and_switch_to_new_window(MainPageLocators.YANDEX_LOGO)
