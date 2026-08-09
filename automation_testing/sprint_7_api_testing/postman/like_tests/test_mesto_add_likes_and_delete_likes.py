import requests
from postman.like_tests import data

def test_mesto_add_likes_and_delete_likes():
       # добавим лайк на фото
    response_put = requests.put(f"{data.URL}/{data.CARD_ID}/likes", headers=data.HEADERS)

    # напиши здесь свой код
    r_likes = response_put.json()['data']['likes']
    print(r_likes)
    print(f'Количество лайков до удаления - ', len(r_likes))
    assert data.MY_USER_ID in r_likes
    response_del = requests.delete(f"{data.URL}/{data.CARD_ID}/likes", headers=data.HEADERS)
    r_del_likes = response_del.json()['data']['likes']
    print(r_del_likes)
    print(f'Количество лайков после удаления - ', len(r_del_likes))
    assert data.MY_USER_ID not in r_del_likes