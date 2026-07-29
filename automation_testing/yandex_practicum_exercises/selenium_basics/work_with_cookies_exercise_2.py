from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# здесь добавь свой предыдущий код для добавления куки
DarthVader_cookie = {"name": "new_cookie", "value": "new_value"}
driver.add_cookie(DarthVader_cookie)

# а теперь измени значение куки
driver.delete_cookie("new_cookie")
DarthVader_cookie = {"name": "new_cookie", "value": "25"}
driver.add_cookie(DarthVader_cookie)
# Проверь новое значение поля value для добавленной куки
assert DarthVader_cookie["value"] == "25"

driver.quit()
