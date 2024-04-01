# Program to Parse a String to a Float or Int

# Solution 1: Parse String into Integer

string = "12345"
print(type(string))

int_string = int(string)
print(type(int_string))

print("----------------------------")

# Solution 2: Parse String to Float

s1 = "123.45"
print(type(s1))

float_string = float(s1)
print(type(float_string))

print("----------------------------")

# Solution 3: Parse String Float Numeral into Integer

s2 = "123.45"
print(type(s2))

str_float_int = int(float(s2))
print(type(str_float_int))

print("----------------------------")


# Program to Convert String to Datetime

# Using Datetime module

from datetime import datetime

date = "Oct 14 1997 7:15AM"
print(type(date))

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time) 
print(type(date_time))

# Using dateutil module

# from dateutil import parser
# date_time1 = parser.parse("Oct 14 1997 7:15AM")
# print(date_time1)
# print(type(date_time1))


# Program to Get a substring of a string

a = "Harry Potter and the Goblet of Fire"
print(a[:12])
print(a[-14:-8])

print("Harry Potter", end=" ")
print("and the Goblet of Fire")


# Program to check if a string is a number(Float)

# Solution 1: Using random module

# import random
# l = [2,5,"a","y",8,"p"]
# random_value = random.choice(l)
# print(random_value)

# Solution 2: Using secret module

import secrets
l = [2,5,"a","y",8,"p"]

random_value = secrets.choice(l)
print(random_value)


# Program to Create a Long multiline string

