import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage
from urls import BASE_URL


@allure.feature('Вопросы о важном')
class TestImportantQuestions:
    @pytest.mark.parametrize('index, expected_answer', FAQ_DATA)
    @allure.title('Ответ FAQ с индексом {index} соответствует вопросу')
    def test_question_opens_correct_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()

        actual_answer = main_page.get_important_answer(index)

        assert actual_answer == expected_answer
