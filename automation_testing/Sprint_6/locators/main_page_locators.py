from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    )
    LOWER_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    )
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    IMPORTANT_QUESTION_0 = (By.ID, 'accordion__heading-0')
    IMPORTANT_ANSWER_0 = (By.ID, 'accordion__panel-0')
    IMPORTANT_QUESTION_1 = (By.ID, 'accordion__heading-1')
    IMPORTANT_ANSWER_1 = (By.ID, 'accordion__panel-1')
    IMPORTANT_QUESTION_2 = (By.ID, 'accordion__heading-2')
    IMPORTANT_ANSWER_2 = (By.ID, 'accordion__panel-2')
    IMPORTANT_QUESTION_3 = (By.ID, 'accordion__heading-3')
    IMPORTANT_ANSWER_3 = (By.ID, 'accordion__panel-3')
    IMPORTANT_QUESTION_4 = (By.ID, 'accordion__heading-4')
    IMPORTANT_ANSWER_4 = (By.ID, 'accordion__panel-4')
    IMPORTANT_QUESTION_5 = (By.ID, 'accordion__heading-5')
    IMPORTANT_ANSWER_5 = (By.ID, 'accordion__panel-5')
    IMPORTANT_QUESTION_6 = (By.ID, 'accordion__heading-6')
    IMPORTANT_ANSWER_6 = (By.ID, 'accordion__panel-6')
    IMPORTANT_QUESTION_7 = (By.ID, 'accordion__heading-7')
    IMPORTANT_ANSWER_7 = (By.ID, 'accordion__panel-7')
