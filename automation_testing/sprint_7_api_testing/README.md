# Sprint 7 — API-тесты Яндекс Самоката

Автотесты API учебного сервиса «Яндекс Самокат».

## Проверяемые ручки

- создание курьера;
- авторизация курьера;
- создание заказа с разными вариантами цвета;
- получение списка заказов.

## Установка зависимостей

```powershell
python -m pip install -r requirements.txt
```

## Запуск тестов и создание результатов Allure

```powershell
python -m pytest --alluredir=allure_results
```

## Просмотр отчёта Allure

```powershell
allure serve allure_results
```
