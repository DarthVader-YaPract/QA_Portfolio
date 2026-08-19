import allure
import pytest

from api.courier_api import CourierApi
from data import ResponseMessages, TestData
from payload_factory import build_courier_data, without_field


@allure.feature("Курьер")
@allure.story("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьера можно создать")
    def test_create_courier_returns_201_and_ok_true(self, courier_cleanup):
        payload = build_courier_data()

        response = CourierApi.create(payload)
        courier_cleanup.append((payload, response.status_code))

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_returns_409(self, registered_courier):
        payload, _ = registered_courier

        response = CourierApi.create(payload)

        assert response.status_code == 409
        assert response.json() == ResponseMessages.COURIER_LOGIN_ALREADY_EXISTS

    @pytest.mark.parametrize("missing_field", TestData.REQUIRED_COURIER_FIELDS)
    @allure.title("Нельзя создать курьера без поля {missing_field}")
    def test_create_courier_without_required_field_returns_400(
        self,
        courier_cleanup,
        missing_field,
    ):
        payload = without_field(build_courier_data(), missing_field)

        response = CourierApi.create(payload)
        courier_cleanup.append((payload, response.status_code))

        assert response.status_code == 400
        assert response.json() == ResponseMessages.CREATE_COURIER_MISSING_DATA

