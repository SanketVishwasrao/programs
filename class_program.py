# Python Program to get the class name of an instance

# Solution 1: Using __class__.__name__

# class SmartPhone:
#     def name(self, name):
#         return name
    
# s1 = SmartPhone()
# print(s1.__class__.__name__)

# Solution 2: Using type() and __name__ attributes

class SmartPhone:
    def name(self, name):
        return name
    
s1 = SmartPhone()
print(type(s1).__name__)


# Program to return multiple values from a function

# Solution 1: Using tuples unpacking

def friends():
    return "Joe", "Phoebe", "Monica"

print(friends())

n1, n2, n3 = friends()
print(n1, ",", n2, "and", n3)

# Solution 2: Using a dictionary

def frd():
    n1 = "Joe"
    n2 = "Phoebe"

    return {1: n1, 2: n2}

print(frd())

names = frd()
print(names[1], ",", names[2])