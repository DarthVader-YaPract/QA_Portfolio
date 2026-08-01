from selenium.webdriver.common.by import By


class StatusPageLocators:
    NOT_FOUND_IMAGE = (By.XPATH, "//img[contains(@src, 'not-found')] | //div[contains(@class, 'Track_NotFound')]")

