# 1) Create the tuple t1 with the following values: 2, “cat”, “a”, -2, “Anna”
# 2) Delete the value “a” from t1 and print t1 afterwards
# 3) Create the tuple t2 with the following values: 1, 2, 3, 4, 5
# 4) Create the tuple t3. The first 2 values of t3 should be the first 2 values of the
# tuple t1, and the last 3 values of t3 should be the first 3 values of the tuple t2
# 5) Print the value at index 2 from the tuple t3
# 6) Create a list of tuples t4 with the following value: [(1,3,5), (8,9), (“Anna”, “Bob”,
# “Alice”)]։ Print the second value of the first tuple in the list t4.

t1 = (2, "cat", "a", -2, "Anna")
print("t1 before changes: ", t1)

t1 = list(t1)
t1.remove("a")
t1 = tuple(t1)

print("t1 after changes: ", t1)

t2 = (1,2,3,4,5)

from itertools import chain

t3 = (t1[:2], t2[-3:])
t3 = tuple(list(chain.from_iterable(t3)))

print("t3 tuple: ", t3)

print("value of 2nd index from the tuple t3: ", t3[2])

t4 = [(1,3,5), (8,9), ("Anna", "Bob", "Alice")]

print("second value of the first tuple in the list t4: ", t4[0][1])