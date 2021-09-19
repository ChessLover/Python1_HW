# Homework 2 

# Create the list list2, which contains some values of your choice. Get one value, using
# the input() function, and delete the first occurrence of the value from the list list2. Print
# the list list2 before and after the change

list2 = [50, 555, 7, 9, 15, 6, 50, 98, 50]

value_from_user = int(input())

print("List before change: ", list2)

list2.remove(value_from_user)

print("List after change: ", list2)