import allure
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    options = webdriver.FirefoxOptions()
    # Для запуска без окна: pytest --headless
    if request.config.getoption("--headless"):
        options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    yield browser
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Запустить Firefox без окна")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
