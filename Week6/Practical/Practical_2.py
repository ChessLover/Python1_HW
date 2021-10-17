# Create a function that doesn’t take any arguments that returns the following text “HI
# EVERYONE”. Create 2 different decorators, one of them should make the letters of a
# string lowercase and the other one should add the following text to the string “!!!
# Welcome to the party.”. Use the decorators on the function you have created in the first
# step. The final result should look like this: “Hi everyone!!! Welcome to the party.”

def dec1(func): 
    def dec_wrapper():
        s = func()
        return s.lower().capitalize()
    
    return dec_wrapper



def dec2(func): 
    def dec_wrapper():
        s = func()
        return s + "!!! Welcome to the party."
    return dec_wrapper

@dec2
@dec1
def ret_string(): 
    return "HI EVERYONE"


print(ret_string())

