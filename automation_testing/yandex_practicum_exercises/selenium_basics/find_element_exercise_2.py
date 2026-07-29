from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди все элементы
elements = driver.find_element(By.TAG_NAME, "img")
print(elements)

images = driver.find_elements(By.TAG_NAME, "img")
# Проверь, что количество найденных элементов больше одного. Для этого используй метод len()
assert len(images) > 1

# Закрой браузер
driver.quit()
