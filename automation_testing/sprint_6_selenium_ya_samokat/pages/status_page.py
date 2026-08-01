from locators.status_page_locators import StatusPageLocators
from pages.base_page import BasePage


class StatusPage(BasePage):
    def is_not_found_visible(self):
        return self.is_visible(StatusPageLocators.NOT_FOUND_IMAGE)

