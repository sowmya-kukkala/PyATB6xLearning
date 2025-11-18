def before_after_ui_test(func):
    def wrapper():
        print("Before Running Code")
        func()
        print("After Running Code")
    return wrapper


@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Application")

test_ui()