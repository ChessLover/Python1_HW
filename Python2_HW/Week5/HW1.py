# Create a Person class which will have attributes Name, Last Name, Email and Age. 
# Use the Decorator pattern and any additional classes of your choice to implement the following logic:
# If the Person is a child (age<14), s/he wants the information about them printed as follows: 
# *** &&& Name - Last Name - Email &&& ***. Otherwise, print the information like this: &&& Name - Last Name - Email &&&.  


class InformationPrinter:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
  
    def render(self):
        return f'{self.first_name} - {self.last_name} - {self.email}'


class AndWrapper(InformationPrinter):

    def __init__(self, wrapped: InformationPrinter):
        self.wrapped = wrapped
  
    def render(self):
        return f'&&& {self.wrapped.render()} &&&'


class AsteriksWrapper(InformationPrinter):
  
    def __init__(self, wrapped: InformationPrinter):
        self.wrapped = wrapped
  
    def render(self):
        return f'*** {self.wrapped.render()} ***'
    
    
class Person:
  
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age


    def print_information(self):
        printer = InformationPrinter(self.first_name, self.last_name, self.email)

        printer_wrapped_in_and = AndWrapper(printer)
        
        if self.age < 14:
            printer_wrapped_in_asteriks_and = AsteriksWrapper(printer_wrapped_in_and)

            print(printer_wrapped_in_asteriks_and.render())
        else:
            print(printer_wrapped_in_and.render())
            
            
person1 = Person('John', 'Doe', 'john@doe.com', 12)
person1.print_information()

person2 = Person('Jane', 'Doe', 'jane@doe.com', 15)
person2.print_information()