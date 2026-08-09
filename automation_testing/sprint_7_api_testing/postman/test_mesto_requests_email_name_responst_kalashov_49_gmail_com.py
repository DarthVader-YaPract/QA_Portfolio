import requests


# напиши здесь свой код
def test_mesto_email_name_response_acyuality_user_email():
    response = requests.get(
        'https://qa-mesto.praktikum-services.ru/api/users/me',
        headers={
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTY3YTc3YjU5M2Q5MTAwM2Q1MzRhZTMiLCJpYXQiOjE3ODU5MzE0NjEsImV4cCI6MTc4NjUzNjI2MX0.dxfiOGmQwviQwHP5xNJLbm91B1xibQg25pZ65c523_w'
        }
    )

    assert 200 == response.status_code
    value = response.json()
    assert value['data']['email'] == 'kalashov_49@gmail.com'



