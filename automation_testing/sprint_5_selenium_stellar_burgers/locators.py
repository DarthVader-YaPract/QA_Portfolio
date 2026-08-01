
from selenium.webdriver.common.by import By


class Locators:
    # Ссылка «Конструктор» в шапке
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//p[text()='Конструктор']]",
    )

    # Логотип Stellar Burgers в шапке
    LOGO_LINK = (By.CSS_SELECTOR, "a[href='/'] > svg[width='290']")

    # Ссылка «Личный кабинет» в шапке
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/account']")

    # Кнопка «Войти в аккаунт» на главной странице
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка «Оформить заказ» после входа в аккаунт
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Поле «Имя» в форме регистрации
    REGISTRATION_NAME_INPUT = (
        By.XPATH,
        "//label[text()='Имя']/following-sibling::input",
    )

    # Поле «Email» в формах регистрации, входа и восстановления пароля
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input",
    )

    # Поле «Пароль» в формах регистрации и входа
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input",
    )

    # Кнопка «Зарегистрироваться» в форме регистрации
    REGISTRATION_BUTTON = (
        By.XPATH,
        "//button[text()='Зарегистрироваться']",
    )

    # Сообщение об ошибке для пароля короче шести символов
    INCORRECT_PASSWORD_ERROR = (
        By.XPATH,
        "//p[text()='Некорректный пароль']",
    )

    # Ссылка «Войти» в формах регистрации и восстановления пароля
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")

    # Кнопка «Войти» в форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылка «Зарегистрироваться» в форме входа
    REGISTRATION_LINK = (By.CSS_SELECTOR, "a[href='/register']")

    # Ссылка «Восстановить пароль» в форме входа
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")

    # Кнопка «Восстановить» в форме восстановления пароля
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Ссылка «Профиль» в меню личного кабинета
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")

    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Вкладка «Булки» в конструкторе
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")

    # Вкладка «Соусы» в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")

    # Вкладка «Начинки» в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Активная вкладка конструктора
    ACTIVE_CONSTRUCTOR_TAB = (
        By.CSS_SELECTOR,
        "div[class*='tab_tab_type_current']",
    )
