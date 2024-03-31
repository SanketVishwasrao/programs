# dictionaries using for loop

friends = {"Rachel": "Ross", "Monica": "Chandler", "Phoebe": "Joe"}
print(friends)

# Solution 1: with .items()
for key, value in friends.items():
    print(key, ":", value)

print("-----------------------------")
# Solution 2: with keys

for key in friends.keys():
    print(key, ":", friends[key])

print("------------------------------")

# Solution 3: with keys and values

for key in friends.keys():
    print(key)

for i in friends.values():
    print(i)

print("-------------------------------")


# Program to check if a Key is Already Present in a Dictionary

name = input("Enter a key here: ")
if name in friends.keys():
    print("Yes,", name, "is present in list")
