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
# Add some exceptions to your class where it is necessary (at least one general and one
# specific exception).
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
        try: 
            num1 = int(num1)
            return print ("My favorite number is " + str(num1)) 
        except ValueError: 
            return print("Number is not an integer. Please give another number.")
        
    def Read_file(self, filename): 
        f_n = filename + ".txt"
        try: 
            open(f_n)
            return print("File is opened!")
        except Exception: 
            return print("File opening failed. Please check the name of file or location.")
            
    def set_pass(self, new_password):
        self.__password = new_password
        return self.__password
    
    def get_pass(self):
        return self.__password
    
    
p1 = Person("Sona", "Asatryan", 22, "female", True, "abc123")

p1.Favourite_num("False")
p1.Favourite_num(5)
p1.Favourite_num(55.5)
    
    
    
