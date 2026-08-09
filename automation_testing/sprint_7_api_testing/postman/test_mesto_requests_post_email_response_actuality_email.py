import requests

def test_mesto_requests_post_email_response_actuality_email():
    payload = {"email": "The_best@ya.ru", 'password': "angina", "avatar": 'https://iimg.su/i/fByLK2'}
    # напиши здесь свой код
    response = requests.post('https://qa-mesto.praktikum-services.ru/api/signup', data=payload)
    resp_code = response.status_code
    resp_text = response.text
    resp_json = response.json()
    box = resp_json['data']['email']
    print(resp_code)
    print(resp_text)
    print(box)

    assert 201 == resp_code
    assert box == 'The_best@ya.ru'



