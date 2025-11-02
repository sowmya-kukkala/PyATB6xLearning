# You want to check whether a web page loads within 3 seconds (performance test condition).
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time = float(input("Enter the load time: "))
if load_time <= 0:
    print("Can't detect the page load time")
else:
    if load_time < 3:
        print(f"✅ Page loaded in time: {load_time:.2f}")
    else:
        print(f"⚠️ Page load too slow: {load_time:.2f}")
