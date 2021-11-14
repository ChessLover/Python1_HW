# Create a list with the following values: ['a', 0, 2]. Write a program which will go over the list
# using a loop and print the reciprocal of each value from the list (1/x). If there are cases
# when you cannot calculate 1/x for the value, you should cover those by a corresponding
# exception.
# The output of the program should be of the following format:
# The entry is: the current entry of the list
# The reciprocal of the current entry of the list is the value of the reciprocal
# OR
# The entry is: the current entry of the list
# Oops! The exception that occured

l = ['a', 0, 2]

for i in range(len(l)): 
    print("The entry is: ", l[i])
    try: 
        print(1/l[i])
    except Exception: 
        print("Oops! The exception that occured")
    
    