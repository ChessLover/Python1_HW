# Create the function max which gets an undefined number of non-keyword arguments
# and returns the maximum of those. In case the function is called without arguments, it
# should return the text “no numbers given”. Don’t use the in-built functions for calculating
# the maximum value.


def max_value(*argv): 
    
    if len(argv) ==0: 
        return print("No numbers given.")
    
    max_val = argv[0]
    for i in range(len(argv)):
        if argv[i]>max_val: 
            max_val = argv[i]

    return max_val 


m = max_value(1,8, 0, -1, 555)
v = max_value()
l = max_value(9)

print("Maximum value is: ", m)