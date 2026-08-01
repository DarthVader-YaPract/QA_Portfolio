# Sprint 6 — Яндекс Самокат

UI-автотесты учебного сервиса «Яндекс Самокат» на Python с использованием Page Object, Selenium, Firefox, pytest и Allure.

## Покрытие

- восемь вопросов раздела «Вопросы о важном»;
- позитивный сценарий заказа с двумя наборами данных;
- верхняя и нижняя кнопки «Заказать»;
- переходы по логотипам Самоката и Яндекса;
- поиск несуществующего заказа.

## Установка и запуск в PowerShell

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest --alluredir=allure_results
```

Firefox должен быть установлен. Selenium Manager автоматически подберёт `geckodriver` при первом запуске.

Запуск Firefox без окна:

```powershell
python -m pytest --headless --alluredir=allure_results
```

Просмотр отчёта (если Allure CLI установлен):

```powershell
allure serve allure_results
```
