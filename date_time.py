# Program to measure the elapsed time 

# Solution 1: Using time module

import time

starting_time = time.time()
print("hello world")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(num1 + num2)

ending_time = time.time()

print(ending_time - starting_time)

# Solution 2: Using timeit module
# This module is more accurate than time module

from timeit import default_timer as timer
starting_value = timer()
print("hello world")

ending_value = timer()
print(ending_value - starting_value)


# Program to create a Countdown Timer

import time

def countdown(sec):

    while sec:
        mins, secs = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        print(time_format)
        time.sleep(1)
        sec -= 1
    
    print("Stop")

countdown(134)