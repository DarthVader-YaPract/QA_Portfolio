import requests

def test_user_has_valid_age():
    response = requests.get("https://randomuser.me/api/")
    r = response.json()
    assert 50 == r["results"][0]["dob"]["age"]