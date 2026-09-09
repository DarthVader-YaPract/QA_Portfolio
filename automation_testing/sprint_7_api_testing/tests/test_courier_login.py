import allure
import pytest

from api.courier_api import CourierApi
from data import ResponseMessages, TestData
from payload_factory import build_courier_data, generate_random_string, without_field


@allure.feature("Курьер")
@allure.story("Авторизация курьера")
class TestCourierLogin:
    @allure.title("Курьер может авторизоваться, ответ содержит id")
    def test_login_courier_returns_200_and_id(self, registered_courier):
        payload, courier_id = registered_courier
        credentials = {
            "login": payload["login"],
            "password": payload["password"],
        }

        response = CourierApi.login(credentials)

        assert response.status_code == 200
        assert response.json()["id"] == courier_id

    @pytest.mark.parametrize("missing_field", TestData.REQUIRED_LOGIN_FIELDS)
    @allure.title("Нельзя авторизоваться без поля {missing_field}")
    def test_login_without_required_field_returns_400(
        self,
        registered_courier,
        missing_field,
    ):
        payload, _ = registered_courier
        credentials = without_field(
            {"login": payload["login"], "password": payload["password"]},
            missing_field,
        )

        response = CourierApi.login(credentials, request_timeout=10)

        assert response.status_code == 400
        assert response.json() == ResponseMessages.LOGIN_MISSING_DATA

    @pytest.mark.parametrize("incorrect_field", TestData.REQUIRED_LOGIN_FIELDS)
    @allure.title("Нельзя авторизоваться с неверным полем {incorrect_field}")
    def test_login_with_incorrect_credentials_returns_404(
        self,
        registered_courier,
        incorrect_field,
    ):
        payload, _ = registered_courier
        credentials = {
            "login": payload["login"],
            "password": payload["password"],
        }
        credentials[incorrect_field] = generate_random_string(12)

        response = CourierApi.login(credentials)

        assert response.status_code == 404
        assert response.json() == ResponseMessages.ACCOUNT_NOT_FOUND

    @allure.title("Несуществующий курьер не может авторизоваться")
    def test_login_nonexistent_courier_returns_404(self):
        payload = build_courier_data()
        credentials = {
            "login": payload["login"],
            "password": payload["password"],
        }

        response = CourierApi.login(credentials)

        assert response.status_code == 404
        assert response.json() == ResponseMessages.ACCOUNT_NOT_FOUND
