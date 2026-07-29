from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# напиши код для добавления куки
DarthVader_cookie = {"name": "new_cookie", "value": "new_value"}
driver.add_cookie(DarthVader_cookie)

# Проверь поле value для добавленной куки
added_cookie = driver.get_cookie("new_cookie")
assert added_cookie["value"] == "new_value"

driver.quit()
