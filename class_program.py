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