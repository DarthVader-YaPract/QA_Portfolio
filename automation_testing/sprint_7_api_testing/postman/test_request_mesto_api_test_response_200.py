import requests

def test_request_mesto_api_test_response_200():
    response = requests.get(
        'https://qa-mesto.praktikum-services.ru/api/users/me',
        headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTY3YTc3YjU5M2Q5MTAwM2Q1MzRhZTMiLCJpYXQiOjE3ODU5MzE0NjEsImV4cCI6MTc4NjUzNjI2MX0.dxfiOGmQwviQwHP5xNJLbm91B1xibQg25pZ65c523_w'}
    )#токен авторизации использовать свой, если мой уже не подходит

    print('Код ответа - ', response.status_code)
    print(response.text)

    assert 200 == response.status_code
