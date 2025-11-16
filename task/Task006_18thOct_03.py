#Simulate a page loading check using a while loop.
#If page_loaded becomes True within 5 seconds, print success; else timeout.

#Hint: Use a counter (like wait_time) and break condition.
import time

page_loaded = False
wait_time = 0
timeout = 5
while wait_time < timeout:
    page_loaded = input("Is page loaded ? [True/False] : ")
    if page_loaded == "True":
        print("Success")
        break
    time.sleep(1)
    wait_time += 1
else:
    print("Time Out")

# Task details provided during the class

# import time
# import random
#
# wait_time = 0
# page_loaded = False
#
#
# def api_response():
#     return random.choice([False, True])
#
#
# while wait_time < 5:
#     page_loaded = api_response()
#     if page_loaded:
#         print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
#         break
#     else:
#         print(f"⏳ Checking... (second {wait_time + 1})")
#         time.sleep(1)  # wait for 1 second
#         wait_time += 1
#
# if not page_loaded:
#     print("❌ Timeout! Page failed to load within 5 seconds.")




