# Program to represent enum

# Using enum module

from enum import Enum

class SmartPhones(Enum):
    Samsung = 1
    Nokia = 2
    Apple = 3

print(SmartPhones.Samsung)
print(SmartPhones.Samsung.name)
print(SmartPhones.Samsung.value)