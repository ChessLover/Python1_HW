# Create a function that takes one required argument name of type String and an
# undefined number of optional non-keyword arguments. The function should calculate the
# average value of the optional arguments (if at least one optional argument is given) and
# print the following: if at least one optional argument is given print “X, your average grade
# is: Y”, where X is the value of the argument name and Y is the average value of the
# optional arguments. Otherwise, print “No grades available for X”, where X is the value of
# the argument name.

def opt_avg (name, *argv): 
    
    if len(argv)>0: 
        avg_value = sum(argv) / len(argv)
        print("%s, your average grade is %d." %(name,avg_value))
        return avg_value
    
    else: 
        return print("No grades available for %s." %name)
    
a = opt_avg("Sona", 1,2,3,4,5,100)
b = opt_avg("Robert")
a = opt_avg("Maria", 99)

