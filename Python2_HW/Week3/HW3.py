# Use singleton pattern and classes of your choice. 
# Create a structure where you have some resource that has states busy and free and 3 users that
# try to use the resource and change the state to busy while they are using it. 
# The resource should be singleton. Implement using 2 different methods for singleton implementation that we have discussed. 
# ---------------------------------------------------------------------------------------

print("------------------------------------------------------------")
print("Method1 : Monostate/Borg Singleton Design pattern")
print("------------------------------------------------------------")


class Singleton_1: 
    
    __current_state = dict()

    def __init__(self): 
        self.__dict__ = self.__current_state
        
    
    def resource_busy(self, resource): 
        self.state = resource


user1 = Singleton_1()
user1.resource_busy('busy')

print(user1.state)

user2 = Singleton_1()
user2.resource_busy('free')

print(user2.state)

user3 = Singleton_1()
user3.resource_busy('busy')

print(user3.state)

print("------------------------------------------------------------")
print("Method2: Classic implementation of Singleton Design Pattern")
print("------------------------------------------------------------")


class Singleton_2: 
    
    __current_state = 'busy'

    def __init__(self): 
        
        if Singleton_2.__current_state != 'busy': 
            raise Exception ("Resource is busy. Try later.")
        else: 
            Singleton_2.__current_state = self 
            
    
    def get_state(self): 
        
        if Singleton_2.__current_state == 'busy':
            Singleton_2()
        return Singleton_2.__current_state
        

user1 = Singleton_2()
print(user1.get_state())

#user2 = Singleton_2()
#print(user2.get_state())

    