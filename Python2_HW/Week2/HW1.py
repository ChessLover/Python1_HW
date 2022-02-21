# You know that each BankAccount object has attributes id, balance and rate. Use builder pattern
# and any extra classes and methods that you may need to realize the creation of a BankAccount type
# object. Create some objects and do some operations to test your classes.

# ---------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Builder(ABC): 
    
    @abstractmethod
    def create_id(self): 
        pass
        
    @abstractmethod
    def create_balance(self): 
        pass
    
    @abstractmethod
    def create_rate(self):        
        pass 
    

class BankAccount(Builder):
    
    def __init__(self): 
        self.account = Account()


    def create_id(self, acc_id): 
        self.account.add_attr(acc_id)
        
        
    def create_balance(self, acc_balance): 
        self.account.add_attr(acc_balance)
        
        
    def create_rate(self, acc_rate): 
        self.account.add_attr(acc_rate)
        

class Account():
    def __init__(self): 
        self.account = []
    
    def add_attr(self, attr): 
        self.account.append(attr)

    def print_list(self): 
        print(*self.account, sep=' -> ')


# ---------------------------------------------------------------------------------------

a = BankAccount()

a.create_id("Sona")
a.create_balance("5000")
a.create_rate("1")

a.account.print_list()


