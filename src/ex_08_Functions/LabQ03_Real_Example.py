def validate_status_code(response_code):
    if response_code > 0:
        if response_code == 200:
            print("Request is successful")
        else:
            print("Error in the request")
    else:
        print("Error in the response code value")

validate_status_code(200)   # Request is successful
validate_status_code(404)   # Error in the request
validate_status_code(response_code=500) # Error in the request
validate_status_code(int(input("Enter your status code: ").strip()))
