# Practical 5

# Create the set set3 containing the values of type int of your choice. Get one
# value, using the input() function, and check if the value is between the minimum and
# maximum values of the set set3 (min<value<max). Print True (it is) or False (it is not)
# accordingly.


set3 = {0, 1, 5, 98, 5, 55, 26, 1}

input_num = int(input())

if (input_num > min(set3)) and (input_num < max(set3)): 
    print(True)
else: 
    print(False)