from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_data import MESTO_EMAIL, MESTO_PASSWORD

driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://qa-mesto.praktikum-services.ru/")

# Авторизация
driver.find_element(By.ID, "email").send_keys(MESTO_EMAIL)
driver.find_element(By.ID, "password").send_keys(MESTO_PASSWORD)
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Ждём загрузки страницы после авторизации
WebDriverWait(driver, 10).until(
    expected_conditions.url_to_be(
        "https://qa-mesto.praktikum-services.ru/"
    )
)

# Нажимаем на изображение профиля
driver.find_element(By.CLASS_NAME, "profile__image").click()

# Вводим ссылку на новый аватар
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"

driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Сохраняем новое изображение
driver.find_element(
    By.XPATH,
    "/html/body/div/div/div[4]/div/form/button[2]"
).click()

# Ждём появления новой ссылки в атрибуте style
WebDriverWait(driver, 10).until(
    expected_conditions.text_to_be_present_in_element_attribute(
        (By.CLASS_NAME, "profile__image"),
        "style",
        avatar_url
    )
)

# Получаем style элемента с изображением
avatar = driver.find_element(By.CLASS_NAME, "profile__image")
style = avatar.get_attribute("style")

# Проверяем ссылку
assert avatar_url in style

driver.quit()
