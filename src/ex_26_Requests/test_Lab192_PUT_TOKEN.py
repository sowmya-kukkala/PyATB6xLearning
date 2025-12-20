import pytest
import requests
import allure

base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

def get_token():

    base_path = "/auth"
    full_url = base_url + base_path

    json_payload_auth = {
                         "username": "admin",
                         "password": "password123"
    }

    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    # print(token)
    assert type(token) == str
    assert len(token) > 0
    return token

def create_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url, headers=headers, json=payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id

def test_put():
    token = get_token()
    booking_id = create_booking_id()
    base_path = "/booking/"+str(booking_id)
    full_url = base_url + base_path
    cookie = "token=" + token

    headers = {"Content-Type": "application/json",
               "Cookie": cookie}

    json_payload = {
        "firstname": "Charlie",
        "lastname": "Evans",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.put(url=full_url, headers=headers, json=json_payload)
    assert response_data.status_code == 200
    assert response_data.json()["firstname"] == "Charlie"

def test_delete():
    token = get_token()
    booking_id = create_booking_id()
    delete_path = "/booking/"+str(booking_id)
    full_url = base_url + delete_path
    cookie = "token=" + token
    headers = {"Content-Type": "application/json", "Cookie": cookie}
    response_data = requests.delete(url=full_url, headers=headers)
    assert response_data.status_code == 201