from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    ORDER_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Go!']")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"

