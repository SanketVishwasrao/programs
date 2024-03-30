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
