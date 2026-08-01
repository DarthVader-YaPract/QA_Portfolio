import secrets
import string

from data import TestData


def generate_email(number=None):
    email_number = number if number is not None else secrets.randbelow(900) + 100

    if not 100 <= email_number <= 999:
        raise ValueError("Номер для email должен состоять из трёх цифр")

    return (
        f"{TestData.EMAIL_NAME}_{TestData.EMAIL_SURNAME}_"
        f"{TestData.COHORT_NUMBER}_{email_number}"
        f"@{TestData.EMAIL_DOMAIN}"
    )


def generate_password(length=8):
    if length < 6:
        raise ValueError("Длина пароля должна быть не меньше шести символов")

    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))
