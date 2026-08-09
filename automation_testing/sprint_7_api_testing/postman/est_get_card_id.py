import requests


def test_get_card_id():
    url = 'https://qa-mesto.praktikum-services.ru/api/cards'

    response_card_id = requests.get(
        url,
        headers={
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTY3YTc3YjU5M2Q5MTAwM2Q1MzRhZTMiLCJpYXQiOjE3ODYwMjAyOTQsImV4cCI6MTc4NjYyNTA5NH0.quiwa6z5C0o3tFHuN_Je3W_oYVWJdYdxkh_4gCBxVtg'
        }
    )

    print(response_card_id.json())
