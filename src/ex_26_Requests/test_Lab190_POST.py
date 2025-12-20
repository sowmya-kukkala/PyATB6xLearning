import pytest
import allure
import requests

@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the Create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    headers = {"Content-Type": "application/json"}

    payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
                            "checkin" : "2018-01-01",
                            "checkout" : "2019-01-01"
                        },
        "additionalneeds" : "Breakfast"
        }

    response_data = requests.post(url = full_url, headers = headers, json = payload)
    assert response_data.status_code == 200
    # Convert response into Json
    response_data_json = response_data.json()

    # BookingID > 0 and firstname == "Jim"

    booking_id = response_data_json["bookingid"]
    first_name = response_data_json["booking"]["firstname"]
    print(booking_id)
    print(first_name)

    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    assert first_name == "Jim"
    assert type(first_name) == str

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = response_data.elapsed.total_seconds()
    assert time < 3

@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify the invalid payload Booking!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}

    json_payload = {}
    response = requests.post(url = URL, headers = headers, json = json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"


