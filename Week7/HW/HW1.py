# Create the class Person.
# Attributes: name, last_name, age, gender, student (this is a boolean attribute i.e.it
# takes values True/False), as well as a private attribute password
# Methods:
# Greeting(self, second_person) - gets an object of type Person as an input and prints
# “Welcome dear X.”, where X is the value of the name attribute of second_person.

# Goodbye(self) - prints “Bye everyone!”

# Favourite_num(self, num1) - gets an integer num1 as an input and returns the text “My
# favourite number is num1”, using the value of the attribute num1.

# Read_file(self, filename) - gets a String filename as an input and tries to read the file
# with the name “filename.txt”, adding “.txt” at the end of the value of the attribute
# filename. Use the function open() to open the file.

# Add set and get methods for the attribute password.
# Optional: Add a decorator which will check how long does it take to execute the method
# Greeting.

import time

def dec(func):
    def dec_wr(self, person): 
        start = time.time()
        # print(start)
        func(self, person)
        end = time.time()
        # print(end)
        
        final= end - start        
        return final        
    return dec_wr


class Person: 
    def __init__(self, name, last_name, age, gender, student, password): 
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password
      
    @dec
    def Greeting(self, second_person): 
        return print("Welcome dear %s." %second_person.name)
        
    def Goodbye(self): 
        print("Bye everyone!")
        
    def Favourite_num(self, num1): 
        return print ("My favorite number is " + str(num1)) 
    
    def Read_file(self, filename): 
        f_n = filename + ".txt"
        open(f_n)
        return print("File is opened!")
    
    def set_pass(self, new_password):
        self.__password = new_password
    
    def get_pass(self):
        return self.__password
        
p1 = Person("Sona", "Asatryan", 22, "female", True, "abc123")
p2 = Person("Susik", "Gaboyan", 25, "female", False, "def456")

print("Time to execute method: ", p1.Greeting(p2))


p1.Goodbye()
p1.Favourite_num(5)
p1.Read_file("test")

print("Password for p1 person is ", p1.get_pass())



