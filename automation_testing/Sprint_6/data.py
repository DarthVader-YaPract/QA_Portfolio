from datetime import date, timedelta


ANATOLIY_ORDER_DATA = {
    'first_name': 'Анатолий',
    'last_name': 'Чумак',
    'address': 'город Кореновск, улица Афанасия Медведева, дом 18',
    'metro_station': 'Парк Победы',
    'phone': '+79053252525',
    'delivery_date': (date.today() + timedelta(days=3)).strftime('%d.%m.%Y'),
    'rental_period': 'двое суток',
    'color': 'black',
    'comment': 'Позвонить за час'
}


VYACHESLAV_ORDER_DATA = {
    'first_name': 'Вячеслав',
    'last_name': 'Фейсов',
    'address': 'Москва, Лубянская площадь, дом 2',
    'metro_station': 'Лубянка',
    'phone': '88000000000',
    'delivery_date': (date.today() + timedelta(days=5)).strftime('%d.%m.%Y'),
    'rental_period': 'трое суток',
    'color': 'black',
    'comment': ''
}


ORDER_DATA = [ANATOLIY_ORDER_DATA, VYACHESLAV_ORDER_DATA]
