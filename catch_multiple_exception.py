# Program to catch multiple exceptions in one line

# Handling multiple exceptions
string = input("Enter something here: ")

try:
    num = int(input("Enter number here: "))
    print(string + num)
except (ValueError, TypeError) as e:
    print(e)

print("Thank U")