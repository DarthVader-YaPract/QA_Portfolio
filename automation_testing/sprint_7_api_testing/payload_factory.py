import random
import string
from copy import deepcopy
from datetime import date, timedelta


def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def build_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }


def build_order_data():
    return {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Москва, улица Тестовая, 1",
        "metroStation": 4,
        "phone": "+7 999 123 45 67",
        "rentTime": 2,
        "deliveryDate": (date.today() + timedelta(days=2)).isoformat(),
        "comment": "Автотест Sprint 7",
    }


def without_field(payload, field):
    changed_payload = deepcopy(payload)
    changed_payload.pop(field)
    return changed_payload

