# Use Factory Method pattern to create 2 different classes PersonalAccount and
# BusinessAccount of type BankAccount having a method CreateAccount with some
# implementation of your choice. Have a BankAccountFactory class and a Client class and allow
# the Client to ask the factory to create an account. The type of the account should be determined
# based on the client’s input. You can decide what should be the client input and how the factory
# class should determine what type of an account to create.


# ---------------------------------------------------------------------------------------

class PersonalAccount: 
    def __init__(self):
        self.acc = "Personal"

    def CreateAccount(): 
        return print("This is a personal account.")


class BusinessAccount: 
    def __init__(self):
        self.acc = "Business"

    def CreateAccount(): 
        return print("This is a business account.")

    
    
# ---------------------------------------------------------------------------------------

class BankAccountFactory: 
    
    def __init__(self):
        self.acc = input("What type of account you want to create? : ")
        
    
class Client(BankAccountFactory): 

    def __init__(self):
        BankAccountFactory.__init__(self)

    def acc_creation(self): 
        
        if self.acc == "Personal": 
            return PersonalAccount.CreateAccount()
        elif self.acc == "Business": 
            return BusinessAccount.CreateAccount()
        else: 
            return print("Please specify Personal or Business account type.")
        


# ---------------------------------------------------------------------------------------  

cl = Client()
cl.acc_creation()