import requests

def test_request_randomuser_api_response_gender():
    response = requests.get("https://randomuser.me/api/")
    r = response.json()

    print(r)
    print(r["results"][0]["gender"])
    gender = r["results"][0]["gender"]
    assert gender == 'female'