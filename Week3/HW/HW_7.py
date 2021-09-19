# Homework 4

# Do the previous exercise creating a new list and making the required changes on it,
# without changing the list list4.

list4 = [0, 1, 2, 9, 15, 6, 50, 98, 50]

print("Given list: ", list4)

print("list3[0]: ", list4[0])
print("list3[4]: ", list4[4])
print("list3[5]: ", list4[5])

list5 = list4.copy()

list5.pop(0)
list5.pop(3) # as we removed 1 item, value in 4th index now is in 3th index
list5.pop(3) # as we removed 2 items, value in 5th index now is in 3th index

print("New list with changes: ", list5)