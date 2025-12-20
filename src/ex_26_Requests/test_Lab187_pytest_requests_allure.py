import pytest
import allure
import requests

@allure.title("TC#1 - Verify the GET Request")
@allure.description("Verify the GET Request is basically successful and gives 200 OK as Status Code")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 200

@allure.title("TC#2 - Verify the GET Request - Negative TC")
@allure.description("This TC check booking for -1 and verify the status code is 404")
@pytest.mark.positive
def test_get_request_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 404

