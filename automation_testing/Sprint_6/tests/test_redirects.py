import allure

from pages.main_page import MainPage
from urls import BASE_URL


@allure.feature('Переходы по логотипам')
class TestRedirects:
    @allure.title('Логотип Самоката открывает главную страницу')
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(f'{BASE_URL}order')
        main_page.click_scooter_logo()

        assert main_page.current_url_is(BASE_URL)

    @allure.title('Логотип Яндекса открывает Дзен в новом окне')
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.click_yandex_logo()

        assert main_page.current_url_contains('dzen.ru')
