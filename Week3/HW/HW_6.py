# Homework 3

# Create the list list3, which contains some values of your choice. Delete the values at
# indexes 0, 4 and 5 from the list. Print the list list3 before and after the change.


list3 = [0, 1, 2, 9, 15, 6, 50, 98, 50]


print("List before change: ", list3)

print("list3[0]: ", list3[0])
print("list3[4]: ", list3[4])
print("list3[5]: ", list3[5])

list3.pop(0)
list3.pop(3) # as we removed 1 item, value in 4th index now is in 3th index
list3.pop(3) # as we removed 2 items, value in 5th index now is in 3th index

print("List after change: ", list3)