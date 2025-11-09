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




