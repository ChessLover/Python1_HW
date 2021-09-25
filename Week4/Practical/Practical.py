# Practical 1 

# Create the sets set1 and set2 containing some values of your choice. Print the
# union and the intersection of the 2 sets.

set1 = {1, "blablabla", True}
set2 = {0, "el mi lav", False, True, "blablabla"} 

print("Union: ", set1.union(set2))
print("Intersection: ", set1.intersection(set2))

# --------------------------------------------------------------------------------------
# Practical 2 

# Create the set set3 containing the values of type int of your choice. Get one
# value, using the input() function, and check if the value is between the minimum and
# maximum values of the set set3 (min<value<max). Print True (it is) or False (it is not)
# accordingly.


set3 = {0, 1, 5, 98, 5, 55, 26, 1}

input_num = int(input())

if (input_num > min(set3)) and (input_num < max(set3)): 
    print("The value is between maximum and minimum: ", True)
else: 
    print("The value is between maximum and minimum: ", False)
    

# --------------------------------------------------------------------------------------
# Practical 3

# Create the dictionary dict1 containing some values of your choice. Get a value
# key of type String and a value value of type String, using the input() function. Add the
# values as a key:value pair to the dictionary dict1. Print the dictionary dict1 before and
# after adding the value.

dict1 = {"GM" : "Aronian" , "world_champion" : "Carlsen" }

input_key = input()
input_value = input()


print("dict1 before changes: ", dict1)

dict1[input_key] = input_value

print("dict1 after changes: ", dict1)

# --------------------------------------------------------------------------------------
# Practical 4

# Create the tuple t2 containing some values of your choice. Replace the value at
# index 4 by the value “hello”. Print the tuple t2 before and after the change. Note that the
# tuples are immutable i.e. cannot be modified.

t2 = (1, 55, 3, "a", "b", "Sona")

print("t2 before change: ", t2)

t2 = list(t2)
t2[4] = "hello"
t2 = tuple(t2)

print("t2 after change: ", t2)

# --------------------------------------------------------------------------------------
# Practical 5

# Create a list of tuples l1 with the following values: [(1, “a”), (2, “b”), (3, “c”)].
# Create the dictionary d1, the keys of the dictionary should be the first values of all the
# tuples in l1 and the values should be the second values of all the tuples in l1. You should
# get the following dictionary: {1: “a”, 2: “b”, 3: “c”}։

l1 = [(1, "a"), (2, "b"), (3, "c")]
d1 = dict(l1)
