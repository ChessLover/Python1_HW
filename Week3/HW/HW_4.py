# Homework 1

# Do Problem 1 from the last practical creating a new list which contains both the values
# from list1 and the new values given by the user, don’t make changes to the list list1.

list1 = ["hello", 1, True] 
value1 = input("Input some value: ")

print("Initial list: ", list1)

new_list = list1.copy()
new_list.append(value1)

print("Newly created list with changes: ", new_list)