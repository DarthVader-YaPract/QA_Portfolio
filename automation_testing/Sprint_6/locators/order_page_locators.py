from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )
    LAST_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )
    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )
    METRO_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )
    PARK_POBEDY_METRO_STATION = (
        By.XPATH,
        "//div[contains(@class, 'Order_Text') and text()='Парк Победы']"
    )
    LUBYANKA_METRO_STATION = (
        By.XPATH,
        "//div[contains(@class, 'Order_Text') and text()='Лубянка']"
    )
    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    TWO_DAYS_RENTAL_PERIOD = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and text()='двое суток']"
    )
    THREE_DAYS_RENTAL_PERIOD = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and text()='трое суток']"
    )
    BLACK_COLOR_CHECKBOX = (By.ID, 'black')
    GREY_COLOR_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    )
    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') "
        "and contains(text(), 'Заказ оформлен')]"
    )
