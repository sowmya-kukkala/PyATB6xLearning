# Take the input from User on Test type they want to run
print("Enter the Test type you want to run")
test_type = input("Enter any one of the Test Type as follows - API, UI, Performance, Security: \n")

match test_type:
    case "API":
        print("We are running POSTMAN API test cases")
    case "UI":
        print("We are running Selenium test cases")
    case "Performance":
        print("We are running Performance test cases")
    case "Security":
        print("We are running Security test cases")
    case _:
        print("Invalid input")

# if - elseif - else
# if test_type == "API":
#     print("We are running POSTMAN API test cases")
# elif test_type == "UI":
#     print("We are running Selenium test cases")
# elif test_type == "Performance":
#     print("We are running Performance test cases")
# elif test_type == "Security":
#     print("We are running Security test cases")
# else:
#     print("Invalid input")


