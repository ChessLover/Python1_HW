# Homework 5

# Problem 4.
# ● Create the list a with the following values: 1, 4, 5, 7, 8, -2, 0, -1
# ● Print the values of list a at indices 3 and 5
# ● Sort the list a in a decreasing order and assign the newly obtained list to the variable a_sorted, the list a should not be changed
# ● Print the 2 sublists of the list a_sorted containing the indices 1...3 and 2...6
# ● Delete the values at indices 2 and 3 from a_sorted
# ● Print the list a_sorted
# ● Create the list b with the following values: "grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"
# ● Sort the list b in an increasing order and assign the newly obtained list to the variable b_sorted, the list b should not be changed
# ● Create a new list c. The first 3 values of the list c should be the elements from the list a at indices 1...3 and the last values of the list c should be the elements from the list b at indices 4...6.
# - Print the list c


a = [1, 4, 5, 7, 8, -2, 0, -1]

print("List value at 3rd index: ", a[3])
print("List value at 5th index: ", a[5])

a_sorted = a.copy()
a_sorted.sort(reverse=True)

print("List values [1:3]: ", a_sorted[1:4])
print("List values [2:6]: ", a_sorted[2:7])

a_sorted.pop(2)
a_sorted.pop(2)

print("List after deleting 2 values: ", a_sorted)

b = ["grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]

b_sorted = b.copy()
b_sorted.sort()

c = []
c.extend(a[1:4])
c.extend(b[4:7])

print("List c: ", c)