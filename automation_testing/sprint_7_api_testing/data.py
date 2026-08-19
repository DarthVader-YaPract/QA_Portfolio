class ResponseMessages:
    CREATE_COURIER_MISSING_DATA = {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи",
    }
    COURIER_LOGIN_ALREADY_EXISTS = {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой.",
    }
    LOGIN_MISSING_DATA = {
        "code": 400,
        "message": "Недостаточно данных для входа",
    }
    ACCOUNT_NOT_FOUND = {
        "code": 404,
        "message": "Учетная запись не найдена",
    }


class TestData:
    REQUIRED_COURIER_FIELDS = ("login", "password", "firstName")
    REQUIRED_LOGIN_FIELDS = ("login", "password")
    ORDER_COLORS = (
        ("black", {"color": ["BLACK"]}),
        ("grey", {"color": ["GREY"]}),
        ("both", {"color": ["BLACK", "GREY"]}),
        ("without_color", {}),
    )
