# Let say you want to send a message to someone. 
# You have 2 options - you can Email the message or SMS the message to the corresponding person. 
# So, you have two options to send the message and the client side code will use one of the implementations to send the message to the corresponding person. 
# Use Bridge Design Pattern to implement the logic with classes of your choice and make sure to test the implementation with some concrete objects.


from abc import ABC, abstractmethod

class Message(ABC): 
    
    @abstractmethod 
    def message(self, msg_text_text): 
        pass
    

class SMS(Message): 
    
    def message(self, msg_text):         
        print ("I am sending a message to you via SMS: ", msg_text)
    
    
class Email(Message): 
    
    def message(self, msg_text):         
        print ("I am sending a message to you via Email: ", msg_text)    
    
class SendMessage: 
    
    
    def __init__(self, msg_text, msg):
        
        self.msg_text = msg_text 
        self.msg = msg
        
    
    def send_message(self, msg_text, msg): 
        
        self.msg.message(self.msg_text)


message_text_to_send = input("Enter text for sending: ")

user1 = SendMessage(message_text_to_send, SMS())
user1.send_message(message_text_to_send, SMS())

user2 = SendMessage(message_text_to_send, Email())
user2.send_message(message_text_to_send, Email())