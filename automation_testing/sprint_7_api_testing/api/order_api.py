import allure
import requests

from urls import Urls


class OrderApi:
    TIMEOUT = 60

    @staticmethod
    @allure.step("Создать заказ")
    def create(payload):
        return requests.post(Urls.ORDERS, json=payload, timeout=OrderApi.TIMEOUT)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_list(params=None):
        return requests.get(
            Urls.ORDERS,
            params=params,
            timeout=OrderApi.TIMEOUT,
        )

    @staticmethod
    @allure.step("Отменить заказ с трек-номером {track}")
    def cancel(track):
        return requests.put(
            f"{Urls.ORDERS}/cancel",
            params={"track": track},
            timeout=OrderApi.TIMEOUT,
        )
