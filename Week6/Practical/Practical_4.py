# Create the generator function power(max) which calculates and yields the powers of 2,
# from 0 to the given integer max one by one. Example: if we call power(3) with max=3 it
# should yield the values 2^0, 2^1, 2^2, 2^3 one by one.


def power(max): 
    for i in range(max+1): 
        yield 2**i
    
n = power(5)

print(list(n))


