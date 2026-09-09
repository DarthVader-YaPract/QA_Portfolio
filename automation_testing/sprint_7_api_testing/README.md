# Sprint 7 — API-тесты Яндекс Самоката

Автотесты API учебного сервиса «Яндекс Самокат», выполненные в рамках
финального проекта 7-го спринта Яндекс Практикума.

## Проверяемые ручки

- создание курьера;
- авторизация курьера;
- создание заказа с разными вариантами цвета;
- получение списка заказов.

## Установка зависимостей

Перейти в папку проекта:

```powershell
cd D:\QA\QA_Portfolio\automation_testing\sprint_7_api_testing
```

Установить зависимости:

```powershell
python -m pip install -r requirements.txt
```

## Запуск тестов и создание результатов Allure

```powershell
python -m pytest --alluredir=allure_results --clean-alluredir
```

## Просмотр отчёта Allure

```powershell
allure serve allure_results
```
