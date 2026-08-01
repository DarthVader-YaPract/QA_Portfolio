import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить данные заказчика")
    def fill_customer_form(self, order):
        self.type_text(OrderPageLocators.FIRST_NAME_INPUT, order["first_name"])
        self.type_text(OrderPageLocators.LAST_NAME_INPUT, order["last_name"])
        self.type_text(OrderPageLocators.ADDRESS_INPUT, order["address"])
        self.type_text(OrderPageLocators.METRO_INPUT, order["metro"])
        self.click(OrderPageLocators.metro_option(order["metro"]))
        self.type_text(OrderPageLocators.PHONE_INPUT, order["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить параметры аренды")
    def fill_rental_form(self, order):
        self.type_text(OrderPageLocators.DATE_INPUT, order["date"])
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rental_period_option(order["rental_period"]))
        self.click(OrderPageLocators.color_checkbox(order["color"]))
        self.type_text(OrderPageLocators.COMMENT_INPUT, order["comment"])

    @allure.step("Оформить и подтвердить заказ")
    def submit_order(self):
        self.click(OrderPageLocators.FORM_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_successful(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL)

