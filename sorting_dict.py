# Program to sort a dictionary by Value

marks = {"John": 23, "Lisa": 56, "Sid" : 48}

sorted_values = sorted(marks.items(), key = lambda x: x[1]) # 1 indicates values and 0 indicates key
print(sorted_values)
print("---------------------------")

# Sort only the values

v = sorted(marks.values())
print(v)