import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    METRO_STATIONS = {
        'Парк Победы': OrderPageLocators.PARK_POBEDY_METRO_STATION,
        'Лубянка': OrderPageLocators.LUBYANKA_METRO_STATION,
    }
    RENTAL_PERIODS = {
        'двое суток': OrderPageLocators.TWO_DAYS_RENTAL_PERIOD,
        'трое суток': OrderPageLocators.THREE_DAYS_RENTAL_PERIOD,
    }
    COLORS = {
        'black': OrderPageLocators.BLACK_COLOR_CHECKBOX,
        'grey': OrderPageLocators.GREY_COLOR_CHECKBOX,
    }

    @allure.step('Заполнить данные заказчика')
    def fill_customer_data(self, order_data):
        self.enter_text(OrderPageLocators.FIRST_NAME_INPUT, order_data['first_name'])
        self.enter_text(OrderPageLocators.LAST_NAME_INPUT, order_data['last_name'])
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, order_data['address'])
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(self.METRO_STATIONS[order_data['metro_station']])
        self.enter_text(OrderPageLocators.PHONE_INPUT, order_data['phone'])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить условия аренды')
    def fill_rental_data(self, order_data):
        self.enter_text(OrderPageLocators.DELIVERY_DATE_INPUT, order_data['delivery_date'])
        self.press_enter(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(self.RENTAL_PERIODS[order_data['rental_period']])
        self.click(self.COLORS[order_data['color']])
        self.enter_text(OrderPageLocators.COMMENT_INPUT, order_data['comment'])

    @allure.step('Отправить и подтвердить заказ')
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    def is_success_message_visible(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MESSAGE)
