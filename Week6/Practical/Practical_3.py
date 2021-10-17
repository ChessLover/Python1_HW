# Create the generator function list_func(list1) which takes the list list1 as an argument
# and yields its values one by one.

def list_func(my_list): 
    for i in my_list: 
        yield i
    
n = list_func([1,2,3,4,8])

print(next(n))