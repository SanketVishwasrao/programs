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

# Solution 1: Using triple quotations

print('''Hello everyone 
this is my demo file
hope you all will like it''')

print("--------------------------------")

# Solution 2: Using \n

print("Hello everyone\nthis is my demo file\nhope you all will like it")
print("--------------------------------")

# Solution 3: Using \

s = "Hello everyone\n"\
"this is my demo file\n"\
"hope you all will like it"

print(s)

print("--------------------------------")

# Program to trim whitespace from a string

# Solution 1: Using strip() function
s3 = " I  love Python "
print(s3)
print(s3.strip())

# Solution 2: Using Regular Expressions(RegEx)
import re
s4 = " I love Python  "
x = re.sub(r'^\s+|\s+$','',s4)
print(x)

# ^ => circumflex -> starting
# \s => whitespace
# \s+ => multiple times whitespace
# \s+$ => multiple times whitespace at the end


# Program to check if Two strings are Anagram

# anagram => if two strings having equal length and after sorting two strings, then it matches the 
#            values, then these two strings are Anagram


# print("-----------------------------------------")
# print("Program to check Anagram")
# str1 = input("Enter first string: ").lower()
# str2 = input("Enter second string: ").lower()

# if len(str1) == len(str2):
#     s1_sorted = sorted(str1)
#     s2_sorted = sorted(str2)

#     if s1_sorted == s2_sorted:
#         print("The String is an Anagram")
#     else:
#         print("The String is not an Anagram")

# else:
#     print("The String is not an Anagram")


# Program to capitalize the first character of a string

# Solution 1: Using .upper() and slicing concepts

# print("------------------------------------------------------")
# a = input("Enter the string: ")

# temp_str = a[:1].upper() + a[1:].lower()
# print("Capitalize the first character of a string:", temp_str)

# Solution 2: Using .capitalize() method

# print("------------------------------------------------------")

# a = input("Enter the string: ")
# print("Capitalize the first character of a string:", a.capitalize())


# Program to count the number of occurrence of a character in string

# Solution 1: Using for() loop

# print("-----------------------------------------")
# str3 = "Wscubetech"
# char = "e"
# count = 0

# for c in str3:
#     if c == char:
#         count += 1

# print(char,"present in",str3,"is", count,"times")

# Solution 2: Using count function

# print("-----------------------------------------")

# str4 = "wscubetech"
# char1 = "m"
# print(char1, "present in", str4, "is", str4.count(char1), "times")


# Program to convert Bytes to a String
    
print(b'Welcome to Python \xF0\x9F\x98\x83'.decode('utf-8'))