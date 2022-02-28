# Use adapter pattern and classes of your choice. 
# Create a structure where you have 1-2 adaptees that have a method that returns some text in spanish. 
# Have an adapter which will have a method that translates the text to english. 
# Have examples of the usage of your class structure.

# ---------------------------------------------------------------------------------------

class Adoptee_1: 
    
    def __init__(self): 
        self.fruit = input("a, b or c: ")
    
    def spanish_fruits(self): 
        if self.fruit == 'a': 
            return "el aguacate"
        elif self.fruit == 'b':
            return "la banana" 
        elif self.fruit == 'c':
            return 'la cereza'
        else: 
            return "Please specify a, b or c :( I am not as clever as you think."
    

class Adoptee_2: 
    
    def __init__(self): 
        self.num = int(input("1, 2 or 3: "))
    
    def spanish_numbers(self): 
        
        if self.num == 1: 
            return "uno"
        elif self.num == 2: 
            return "dos" 
        elif self.num == 3: 
            return "tres"
        else: 
            return "Please specify 1,2 or 3 :( I am not as clever as you think."
        
        
class Adopter_translator: 
        
    
    def eng_fruits(self): 
        
        ob_fruit = Adoptee_1()       
        
        if ob_fruit.spanish_fruits() == 'el aguacate': 
            print("Spanish version: ", ob_fruit.spanish_fruits())
            return print("English version: avocado")
        elif ob_fruit.spanish_fruits() == 'la banana':
            print("Spanish version: ", ob_fruit.spanish_fruits())
            return print("English version: banana")
        elif ob_fruit.spanish_fruits() == 'la cereza':
            print("Spanish version: ", ob_fruit.spanish_fruits())
            return print("English version: cherry")
        else: 
            return print("Nothing to translate.")       
    
    
    
    def eng_numbers(self):
        
        ob_num = Adoptee_2()
        
        if ob_num.spanish_numbers() == 'uno': 
            print("Spanish version: ", ob_num.spanish_numbers())
            return print("English version: one")
        elif ob_num.spanish_numbers() =='dos': 
            print("Spanish version: ", ob_num.spanish_numbers())
            return print("English version: two") 
        elif ob_num.spanish_numbers() =='tres': 
            print("Spanish version: ", ob_num.spanish_numbers())
            return print("English version: three")
        else: 
            return print("Nothing to translate.")



ob = Adopter_translator()
ob.eng_numbers()
ob.eng_fruits()


