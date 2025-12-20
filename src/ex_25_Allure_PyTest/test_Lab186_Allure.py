# **To See the Allure Report**
#  so if you want to run a pytest with HTML allure report to generate the HTML report,
# > pytest src/ex_25_Allure_Pytest/test_Lab186_Allure.py --alluredir allure-results

# Below command to see the results in localhost (run this once the above command creates the folder)
# allure serve allure-results
import pytest
import allure

@allure.title("#1 Verify that the Create Booking is Working")
@allure.description("We are going to verify the Create Booking in the future of this function")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1 == 2

@allure.title("#2 Verify that Create Booking, with invalid data is working")
@allure.description("This Test Case check for the negative create Booking")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1+1 == 2

@allure.title("#3 Verify that Create Booking, with invalid data is working")
@allure.description("This Test Case check for the negative create Booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1+1 == 2