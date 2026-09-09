import allure
import pytest

from api.courier_api import CourierApi
from api.order_api import OrderApi
from payload_factory import build_courier_data


@pytest.fixture
def courier_cleanup():
    created_couriers = []

    yield created_couriers

    for payload, status_code in created_couriers:
        if status_code == 201:
            login_response = CourierApi.login(
                {
                    "login": payload["login"],
                    "password": payload["password"],
                }
            )
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                with allure.step(f"Удалить тестового курьера с id={courier_id}"):
                    CourierApi.delete(courier_id)


@pytest.fixture
def registered_courier():
    payload = build_courier_data()
    CourierApi.create(payload)
    login_response = CourierApi.login(
        {
            "login": payload["login"],
            "password": payload["password"],
        }
    )
    courier_id = login_response.json()["id"]

    yield payload, courier_id

    CourierApi.delete(courier_id)


@pytest.fixture
def order_cleanup():
    created_order_tracks = []

    yield created_order_tracks

    for track in created_order_tracks:
        if track is not None:
            OrderApi.cancel(track)

