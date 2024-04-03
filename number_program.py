# Program to reverse a number

# Solution 1: Using while() loop

# num = int(input("Enter a number here:")) # 153
# rev_num = 0
# temp_num = num

# while num != 0:
#     temp = num % 10  # 3, 5, 1
#     rev_num = (rev_num * 10) + temp # 3, 35, 351
#     num = num // 10        # 15, 1, 0

# print("Original number: ", temp_num)
# print("Reverse number: ", rev_num)

# Solution 2: Using string slicing

# num = int(input("Enter a number here: "))
# print("Reverse number:", str(num)[::-1])


# Program to compute the power of a number

# Solution 1: Using while loop

# base = int(input("Enter the base number: ")) # 2
# exponent = int(input("Enter the Exponent: ")) # 4

# result = 1

# while exponent != 0: # 4, 3, 2, 1, 0
#     result = result * base  # 2, 4, 8, 16 
#     exponent -= 1  # 3, 2, 1, 0

# print(result) # 16

# Solution 2: Using for loop

# base = int(input("Enter the base number: ")) # 2
# exponent = int(input("Enter the Exponent: ")) # 4

# result = 1

# for i in range(1, exponent+1): # 1, 2, 3, 4
#     result = result * base     # 2, 4, 8, 16 

# print(result) # 16

# Solution 3: Using pow() function

# base = int(input("Enter the base number: "))
# exponent = int(input("Enter the Exponent: "))

# print(pow(base, exponent))

# Solution 4: Using Exponentiation operator

# base = int(input("Enter base number: "))
# exponent = int(input("Enter exponent number: "))

# print(base**exponent)


# Program to count the number of digits present in a number

# Solution 1: Using while() loop

# num = int(input("Enter the number: ")) # 248
# digits_count = 0

# while num != 0:  # 248, 24, 2, 0
#     num = num // 10  # 24, 2, 0
#     digits_count += 1  # 1, 2, 3

# print("The number of digits present in a number:", digits_count)

# Solution 2: Using len() function

num = int(input("Enter the number: ")) # 248

print("The number of digits present in a number:", len(str(num)))


print("---------------------------------------------")
# Program to add two numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("The sum of given two numbers is", num1 + num2)


# Program to find the square root

# Solution 1: Using Exponentiation

# num1 = int(input("Enter a number: "))
# num2 = 0.5

# print("The square root of the given number is", num1**num2)

# Solution 2: Using Math module

# import math

# num1 = int(input("Enter the number: "))
# print("The square root of given number is",math.sqrt(num1))


# Program to calculate the Area of a triangle

# base = float(input("Enter the base: "))
# height = float(input("Enter the height: "))

# area = (0.5) * base * height
# print("The area of triangle is", area)


# Program to solve quadratic equation

# Quadratic Equation :: ax**2 + b*x + c
# a, b, c are real numbers
# a != 0

# import cmath

# a = int(input("Enter number (a != 0): "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))

# # formula for discriminant

# d = (b ** 2) - (4 * a * c)

# root1 = (-b - cmath.sqrt(d)) / (2*a)
# root2 = (-b + cmath.sqrt(d)) / (2*a)

# print("The roots are", root1, "and", root2)


# Program to swap two variables

# Solution 1: Using third variable

# x = int(input("Enter first number: "))  # 12
# y = int(input("Enter second variable: ")) # 13

# print("Before swapping two variables:")
# print("first number:",x)
# print("second number:",y)
# print()

# temp = x  # 12
# x = y     # 13
# y = temp  # 12

# print("After swapping two variables:")
# print("first number:",x)
# print("second number:",y)

# Solution 2: Without using third variable 

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("Before swapping two variables:")
# print("first number:",x)
# print("second number:",y)
# print()

# x, y = y, x

# print("After swapping two variables:")
# print("first number:",x)
# print("second number:",y)


# Program to generate a random number

# import random 

# x = random.randint(0, 10)
# print(x)


# Program to convert kilometers to miles

# 1 kilometre = 0.621371 mile

# km = float(input("Enter your value in kms: "))
# miles = (0.621371) * km
# print(km, "kms will be", miles, "miles")


# Program to convert Celsius to Fahrenheit

# 0 degree celsius = 32 Fahrenheit

# (celsius * (9/5)) + 32 = Fahrenheit

# celsius = int(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * (9/5)) + 32

# print("Fahrenheit temperature:", fahrenheit, "fahrenheit")


# Program to check if a number is Positive, Negative or zero

# num1 = int(input("Enter the number: "))

# if num1 > 0:
#     print(num1,"is positive number")
# elif num1 == 0:
#     print("It is zero")
# else:
#     print(num1,"is negative number")


# Program to check if a number is Odd or Even

# num1 = int(input("Enter the number: "))
# if num1 % 2 == 0:
#     print(num1, "is even")
# else:
#     print(num1, "is odd")


# Program to check leap year

# year = int(input("Enter the year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# Program to find the largest among three numbers

# num1 = int(input("Enter the value of num1: "))
# num2 = int(input("Enter the value of num2: "))
# num3 = int(input("Enter the value of num3: "))

# if num1 > num2 and num1 > num3:
#     print(num1, "is the largest among three numbers")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is the largest among three numbers")
# else:
#     print(num3, "is the largest among three numbers")


# Program to check prime number

# num1 = int(input("Enter the number: "))

# if num1 == 1:
#     print(num1, "is not a prime number")
# elif num1 > 1:
#     for i in range(2, num1//2 + 1):
#         if num1 % i == 0:
#             print(num1, "is not a prime number")
#             break
#     else:
#         print(num1, "is a prime number")


# Program to print all the prime numbers in an interval

# lower_interval = int(input("Enter lower range: "))  # 5
# upper_interval = int(input("Enter upper range: "))  # 15
# lst = []

# # Ans ====>  5, 7, 11, 13

# if lower_interval < upper_interval:
#     for i in range(lower_interval, upper_interval + 1):
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
# else:
#     print("Please enter lower range value is less than upper range value")

# if len(lst) > 0:
#     print(lst)


#  Program to find the factorial of a number

# Solution 1: Using for loop

# num1 = int(input("Enter a number: "))
# fact = 1

# if num1 == 0:
#     print("Factorial of", num1, "is 1")
# elif num1 > 1:
#     for i in range(1, num1 + 1):
#         fact *= i
# else:
#     print("Factorial of negative doesn't exist")

# print("Factorial of", num1, "is", fact)

# Solution 2: Using recursion

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)
    
# num1 = int(input("Enter a number: "))
# print("The factorial of", num1, "is", factorial(num1))


# Program to display the multiplicatio table

# Solution 1: Using for loop

# num1 = int(input("Enter the number: "))
# print("The multiplication table of", num1, "is:")

# for i in range(1, 11):
#     print(num1, "*", i, "=", (num1*i))

# Solution 2: Using while loop

# num1 = int(input("Enter the number: "))
# print("The multiplication table of", num1, "is:")
# i = 1

# while i < 11:
#     print(num1, "*", i, "=", (num1 * i))
#     i += 1


# Program to print the Fibonacci sequence

# a = 0
# b = 1

# terms = int(input("Enter the number of terms: "))

# print(a, b, end=" ")

# for i in range(terms-2):
#     c = a + b
#     print(c, end=" ")
#     a = b
#     b = c


# Program to check Armstrong Number

# num1 = int(input("Enter the number: "))  # 153
# temp = num1  # 153
# sum = 0
# digits_count = 0
# lst = []

# while temp != 0:  # 153, 15, 1
#     a = temp % 10      # 3, 5, 1
#     lst.append(a)      # [3, 5, 1]
#     temp = temp // 10  # 15, 1, 0
#     digits_count += 1  # 1, 2, 3

# for i in range(len(lst)):
#     sum  = sum + lst[i]**digits_count # 27, 152, 153

# if sum == num1:
#     print(num1, "is an armstrong number")
# else:
#     print(num1, "is not an armstrong number")


# Program to find the Armstrong number in an interval

# lower_limit = int(input("Enter lower limit: "))
# upper_limit = int(input("Enter upper limit: "))
# armstrong_number_lst = []

# for num1 in range(lower_limit, upper_limit + 1):
#     sum = 0
#     temp = num1
#     digits_count = len(str(num1))

#     while temp != 0:
#         a = temp % 10
#         sum = sum + a ** digits_count
#         temp = temp // 10

#     if sum == num1:
#         armstrong_number_lst.append(num1)

# print("Armstrong numbers in range of", lower_limit, "and", upper_limit, 
#     "is", armstrong_number_lst)


# Program to find the sum of natural numbers

# num1 = int(input("Enter a number: "))
# sum = 0

# if num1 < 0:
#     print("Please enter positive number")
# else:
#     while num1 != 0:
#         sum += num1
#         num1 -= 1

# print("Sum of natural number is", sum)



# Program to find numbers divisible by another number

# Solution 1: Using for() loop

# print("The numbers divisible by 13 are: ")
# for i in range(1, 100):
#     if i % 13 == 0:
#         print(i, end=" ")

# Solution 2: Using lambda function and filter function

# print("The numbers divisible by 13 are:", end=" ")
# l = [39, 48, 26, 98, 33, 67, 87]

# result = list(filter(lambda x: x % 13 == 0, l))

# print(result)


# Program to convert Decimal to Binary, Octal and Hexadecimal

# decimal = int(input("Enter number here: "))
# print("The conversion of decimal number", decimal, "is: ")

# print(bin(decimal), "in binary")        # prefix of binary => 0b
# print(oct(decimal), "in octal")         # prefix of octal => 0o
# print(hex(decimal), "in hexadecimal")   # prefix of hexadecimal => 0x


# Program to find ASCII value of character

# Use of ord() function

# char = '%'
# print("The ASCII value of", char, "is", ord(char)) 


# Program to find HCF or GCD

# def calcHCF(x, y):
#     hcf = 1
#     if x > y:
#         smaller = y
#     else:
#         smaller = x

#     for i in range(1, smaller+1):
#         if x % i == 0 and y % i == 0:
#             hcf = i
#     return hcf

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = calcHCF(num1, num2)
# print("The HCF of", num1, "and", num2, "is", result)


# Program to find the factors of a number

# num1 = int(input("Enter a number: "))
# print("The factors of", num1, "are:", end=" ")
# for i in range(1, num1+1):
#     if num1 % i == 0:
#         print(i, end=" ")


# Program to make a simple calculator

# print("~~~~Mini Calculator~~~~")

# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))
# result = 0

# print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division")

# choice = int(input("Enter the choice from 1-4: "))

# if choice == 1:
#     result = num1 + num2
# elif choice == 2:
#     result = num1 - num2
# elif choice == 3:
#     result = num1 * num2
# elif choice == 4:
#     result = num1 / num2
# else:
#     print("Invalid choice")

# print("Result is", result)


# Program to shuffle deck of cards

# import random, itertools

# deck = list(itertools.product(range(1, 14), ['Spade', 'Club', 'Hearts', 'Diamond']))

# random.shuffle(deck)
# print(deck)

# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])


# Program to display Calendar

# import calendar

# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))

# calen = calendar.month(year, month)
# print(calen)


# Program to display Fibonacci sequence using recursion

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# n = int(input("Enter the number of terms: ")) # 5
# if n <= 1: 
#     print("Enter the positive number")
# else:
#     print("Fibonacci sequence:")
#     for i in range(n):
#         print(fibo(i))


# Program to find sum of natural numbers using recursion

# def sum_of_natural_nos(n):
#     if n <= 1:
#         return n
#     else:
#         return n + sum_of_natural_nos(n - 1)

# n = int(input("Enter the no of terms: "))
# if n <= 0:
#     print("Enter positive numbers")
# else:
#     print("Sum of first", n,"natural numbers is", sum_of_natural_nos(n))


# Program to find factorial of number using recursion

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
    
# n = int(input("Enter the number to find out factorial: "))

# if n == 0:
#     print("Factorial of", n, "is", 1)
# elif n < 0:
#     print("Factorial of negative number doesn't exist")
# else:
#     result = fact(n)
#     print("Factorial of", n, "is", result)


# Program to convert Decimal to Binary using Recursion

# def ConvertBinary(n):
#     if n > 1:
#         ConvertBinary(n // 2)
#     print(n % 2, end="")

# ConvertBinary(14)