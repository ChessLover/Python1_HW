# Create the function my_range(n) which gets the value n of type int as an argument and
# yields the values 0, 1, … , n-1, n until it reaches the value n+1 and prints “there are no
# values left”.


def my_range (n): 
    for i in range(n): 
        yield i

n = list(my_range(5))

for i in n: 
    print(n[i])


# I could not understand how to handle value n+1. 