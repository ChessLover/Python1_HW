# Create a function that doesn’t take any arguments and returns the string “Hi”. Create 2
# different decorators: one of them adds the string “, it’s me!” to the value returned by the
# function, the other one adds “<u>” and “</u>” to the value returned by the function. Use
# the decorator so that the final result looks like this:
# <u> Hi, it’s me! </u>


def dec_func1(func): 
    def wrapper(): 
        return func() + ", it's me!"
    return wrapper


def dec_func2(func): 
    def wrapper(): 
        return "<u> " + func() + " </u>"
    return wrapper

@dec_func2
@dec_func1
def empty_func(): 
    return "Hi"

s = empty_func()
print(s)