# Python Program to Access Index of a List Using for loop

# Using enumerate() method

l = [34, 5, 61, 54, 89]

for index, ele in enumerate(l, start=1):
    print(index, "-", ele)

print("---------------------------")

for index, value in enumerate(l):
    print(index, "-", value)

print("----------------------------")

# Without using enumerate() method
    
l1 = [34, 5, 61, 54, 89]
for index in range(len(l1)):
    print(index, "-", l1[index])

# To check if a list is empty

print("----------------------------")

# Solution 1: using boolean operation
# print(bool([]))

my_list = []
if not my_list:
    print("The list is empty")

print("-----------------------------")

# Solution 2: using len() function

l1 = []
if len(l1) == 0:
    print("The list is empty")

print("-----------------------------")

# Solution 3: using []
l2 = []
if l2 == []:
    print("The list is empty")


# Program to Concatenate Two Lists
    
# Solution 1: Using + Operator
print("-----------------------------")

l1 = [3, 6, 8, 2, "a", "j"]
l2 = [3, 6, "k", "f", "j"]

l12 = l1 + l2
print(l12)

print("-----------------------------")

# Solution 2: With unique values

l34 = set(l1 + l2)
print(list(l34))
print("-----------------------------")

# Solution 3: Using extend() function

l1.extend(l2)
print(l1)

# Program to Get the last element of the list

l5 = ["Ironman", "Thor", "Hulk", "Vision"]
print(l5[-1])
print(l5[len(l5) - 1])


# Program to randomly select an element from the list

num = input("Enter something here: ")
def float_check(num):
    try:
        float(num)
        return True
    except:
        return False
    
print(float_check(num))


# Program to count the occurrence of an item in a list

numbers = [10, 20, 50, 40, 10, 30, 10, 20, 40, 70]
count_occurence = numbers.count(18)
print(count_occurence)