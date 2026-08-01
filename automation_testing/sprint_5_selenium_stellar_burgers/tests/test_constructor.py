import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators import Locators


class TestConstructor:
    def test_go_to_buns_tab(self, driver):
        driver.get(Urls.MAIN_URL)
        sauces_tab = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_CONSTRUCTOR_TAB, "Соусы"
            )
        )
        driver.find_element(*Locators.BUNS_TAB).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_CONSTRUCTOR_TAB, "Булки"
            )
        )

    @pytest.mark.parametrize(
        "tab_locator, expected_text",
        [
            (Locators.SAUCES_TAB, "Соусы"),
            (Locators.FILLINGS_TAB, "Начинки"),
        ],
    )
    def test_go_to_constructor_tab(
        self, driver, tab_locator, expected_text
    ):
        driver.get(Urls.MAIN_URL)
        tab = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(tab_locator)
        )
        tab.click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_CONSTRUCTOR_TAB, expected_text
            )
        )
