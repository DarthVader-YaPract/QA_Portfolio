import requests
import json

def test_mesto_req_code_and_link_200_actual_link():
    payload = {"email": "mudlo@ya.ru", 'password': "angina"}
    # напиши здесь свой код
    response = requests.post('https://qa-mesto.praktikum-services.ru/api/signin', data=payload)
    resp_code = response.status_code #запрашиваем код - статус ответа
    resp_json = response.json() # запрашиваем json
    json_string = json.dumps(resp_json) # создаем переменную и присваиваем ей json строку (это всё учебные материалы и тренировка)
    print('Код ответа -', resp_code) # выводим код ответа
    print('Ссылка на аватар: ', resp_json['data']['avatar']) # выводим ссылку на аватар
    print(json_string) # выводим  json строку
    assert 200 == resp_code 
    assert resp_json['data']['avatar'] == 'https://pictures.s3.yandex.net/resources/jacques-cousteau_1604399756.png'