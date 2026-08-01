from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from locators import Locators


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(Urls.MAIN_URL)
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        ).is_displayed()

    def test_login_from_personal_account(self, driver):
        driver.get(Urls.MAIN_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        ).is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.get(Urls.REGISTRATION_URL)
        driver.find_element(*Locators.LOGIN_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        ).is_displayed()

    def test_login_from_forgot_password_form(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        driver.find_element(*Locators.LOGIN_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.LOGIN_BUTTON
            )
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.CORRECT_PASSWORD
        )
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                Locators.ORDER_BUTTON
            )
        ).is_displayed()
