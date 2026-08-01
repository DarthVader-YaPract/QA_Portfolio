class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    MAIN_URL = f"{BASE_URL}/"
    REGISTRATION_URL = f"{BASE_URL}/register"
    LOGIN_URL = f"{BASE_URL}/login"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
    ACCOUNT_URL = f"{BASE_URL}/account"
    PROFILE_URL = f"{BASE_URL}/account/profile"


class TestData:
    USER_NAME = "Андрей Калашов"
    EMAIL_NAME = "andrey"
    EMAIL_SURNAME = "kalashov"
    COHORT_NUMBER = "49"
    EMAIL_NUMBER = 223
    EMAIL_DOMAIN = "ya.ru"
    EMAIL = (
        f"{EMAIL_NAME}_{EMAIL_SURNAME}_{COHORT_NUMBER}_"
        f"{EMAIL_NUMBER}@{EMAIL_DOMAIN}"
    )
    CORRECT_PASSWORD = "12345678"
    INCORRECT_PASSWORD = "12345"
    INCORRECT_PASSWORD_ERROR = "Некорректный пароль"
