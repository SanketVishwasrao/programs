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