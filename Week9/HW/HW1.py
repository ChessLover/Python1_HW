# Create the function div(x, y), which gets 2 attributes x and y and returns the value x/y.
# Inside the function write an assert statement which checks whether the value of y is 0
# and gives an error message “Can’t divide”, in case the condition is not satisfied.


def div(x, y): 
    assert (y == 0), "Can't devide"
    return x/y


a = div(1, 2)
b = div(5, 0)

print(a)
print(b)