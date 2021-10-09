# -------------------------------Problem 1-------------------------------
# Create the variables name, age, password with values of your choice։ Write the
# following program:
# If the value of the variable name is “Batman”, print “Welcome Mr. Batman!” no matter
# what the values of the other variables are. If the value of the variable age <16, print
# “Dear X, you are too young to register”, using the value of the variable name instead of
# X; if the value of the variable password doesn’t contain either ‘*’ or “&”, print “Please
# enter a different password”.

def password_check(name,age,password): 
    if name=="Batman": 
        print("Welcome Mr. Batman!")
    
    if age<16: 
        print("Dear %s, you are too young to register!" %name)
    
    if "*" in password or "&" in password: 
        print("Please enter a different password.")

name = "Sona"
age = 22
password = "alskineinviev"
    
password_check(name,age,password)
password_check("Batman",11,"A*aaabbb&")


# -------------------------------Problem 2-------------------------------
# Print only the odd number 0-100, using a for or a while loop and an if/else statement.

n = 0 

while n<101: 
    if n%2 == 1:
        print(n)
    n += 1

# -------------------------------Problem 3-------------------------------
# Go over the numbers 1-20 in a loop, stop the loop (break) once you reach a number that
# is a multiple of both 3 and 5.

for i in range(1,20): 
    print(i)
    if i%3==0 and i%5==0:
        break