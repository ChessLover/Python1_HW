# Create a function that doesn’t take any arguments and returns the text “Inside the
# function”. Create a decorator which will change the function so that the final result looks
# like this:
# “Before function call”
# “Inside the function”
# “After the function call”
# So, the decorator should add a string values before and after the function call.



def dec_f (func): 
    def inside_f(): 
        print('Before function call')
        func()
        print('After function call')
        
    return inside_f

@dec_f
def f1(): 
    print("Inside the function.")

f1()