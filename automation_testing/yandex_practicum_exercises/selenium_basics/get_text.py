from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_data import MESTO_EMAIL, MESTO_PASSWORD

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
driver.find_element(By.ID, 'email').send_keys(MESTO_EMAIL)

# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, 'password').send_keys(MESTO_PASSWORD)

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, "//button[@class='auth-form__button']").click()

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, "header__logout")
    )
)
# Найди кнопку, получи её текст и проверь, что он равен 'Выйти'
text_log_out = driver.find_element(By.CLASS_NAME, "header__logout")

assert text_log_out.text == "Выйти"

driver.quit()
