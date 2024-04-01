# Program to copy a file

from shutil import copyfile

copyfile("I:/demo.txt", "I:/file.txt")

# Program to Read a file line by line into a list

# Solution 1: Using readlines()

# f = open("file1.txt", "r")
# lines = f.readlines()
# print(lines)

# new_lines = [x.strip() for x in lines]  # strip() method is used to remove "\n"
# print(new_lines)

# Solution 2: Using for loop and List comprehension

# line = [line for line in f]
# print(line)

# new_line = [x.strip() for x in line]  # strip() method is used to remove "\n"
# print(new_line)


# Program to append to a file

f = open("demo.txt", "a")
f.write("\nThis is my demo file")

t = "\nHope you like it"

for i in range(0,5):
    f.write(t)
f.close()


#  Program to Extract extension from the file name

# Solution 1: Using os module

# import os

# file_extension = os.path.splitext("I:/Python/oops/p2.py")
# print(file_extension)
# print(file_extension[1])

# Solution 2: Using pathlib module

# from pathlib import Path

# print(Path("I:/Python/oops/p2.py").suffix)  # It gives extension of file
# print(Path("I:/Python/oops/p2.py").stem)  # It gives file name


# Get the file name from the file path

# Solution 1: Using os module

import os

file_name = os.path.basename("I:/Python/oops/p2.py")
print(os.path.splitext(file_name)[0])

# Solution 2: Using Path module

from pathlib import Path

print(Path("I:/Python/oops/p2.py").stem)