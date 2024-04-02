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