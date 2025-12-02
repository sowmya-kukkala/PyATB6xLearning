class TestCounter:
    count = 0

    def __init__(self):
        TestCounter.count += 1

t1 = TestCounter()
t2 = TestCounter()
print(TestCounter.count) # 2 -> Based on the call value of the count will be increased

# Note: Each time an object is created, count increases.
# Count is shared across all the objects
