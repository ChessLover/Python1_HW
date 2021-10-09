# Create a function that takes password of type String as an argument and check if the
# given password corresponds to the password rules, returning True or False,
# accordingly:
# Password rules:
# The length of the password should be at least 10
# The password should contain at least 2 numbers (try to find how to check this on your
# own)

def password_check(password): 
    if len(password) < 10: 
        print("Password should have 10 characters at least. Try again.")
        return False
    
    count_num = 0
    
    for i in range(len(password)): 
        if password[i].isnumeric()==True: 
            count_num += 1
            
    if count_num >= 2: 
        print("You have a correct password according to our rules!")
        return True
    else: 
        print("Try to use more numbers in your password. Try again.")
        return False
    
    
password_check("alskineinviev")
password_check("1alskineinviev1")
password_check("1alskiv1")
