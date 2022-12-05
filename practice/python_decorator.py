# Instructions
# time.time() will return the current time in seconds since January 1, 1970, 00:00:00
# Try running the starting code to see the current time printed.
# If you run the code after a while, you'll see a new time printed.

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
        
fast_function()
slow_function()