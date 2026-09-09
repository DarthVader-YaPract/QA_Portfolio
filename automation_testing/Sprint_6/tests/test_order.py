import allure
import pytest

from data import ANATOLIY_ORDER_DATA, VYACHESLAV_ORDER_DATA
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL


@allure.feature('Заказ самоката')
class TestOrder:
    @pytest.mark.parametrize(
        'order_data, order_button, order_button_name',
        [
            (
                ANATOLIY_ORDER_DATA,
                MainPageLocators.TOP_ORDER_BUTTON,
                'top',
            ),
            (
                VYACHESLAV_ORDER_DATA,
                MainPageLocators.LOWER_ORDER_BUTTON,
                'lower',
            ),
        ]
    )
    @allure.title(
        'Успешное оформление заказа через кнопку '
        '{order_button_name}'
    )
    def test_order_can_be_created(
        self,
        driver,
        order_data,
        order_button,
        order_button_name,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()

        main_page.start_order(order_button)

        order_page.fill_customer_data(order_data)
        order_page.fill_rental_data(order_data)
        order_page.submit_order()

        assert order_page.is_success_message_visible()
