# Create the class Calculation:
# Attributes: x, y
# Methods: __init__(self, x, y) -> ստեղծում է x ու y attribute-ները
# addition(self) -> տպում է x ու y արգումենտների արժեքների գումարը
# subtraction(self) -> տպում է x ու y արգումենտների արժեքների տարբերությունը
# Ստեղծեք MyCalculation class-ը, որը ժառանգում է Calculation class-ից:
# Attributes: x, y
# Methods: __init__(self, x, y) -> կանչում է Calculation class-ի __init__ method-ը x ու y
# attribute-ներով
# multiplication(self) -> տպում է x ու y արգումենտների արժեքների արտադրյալը
# division(self) -> տպում է x ու y արգումենտների արժեքների քանորդը
# Ստեղծեք MyCalculation class-ի object 3 ու 5 attribute-ների արժեքներով ու կանչեք իր վրա
# addition, subtraction, multiplication ու division method-ները:

class Calculation: 
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def addition(self): 
        return print("Sum of x and y:", self.x+self.y)
    
    def subtraction(self): 
        return print("Sub of x and y:", self.x-self.y)


class MyCalculation(Calculation):
    def __init__(self, x, y): 
        super().__init__(x, y)
        
    def multiplication(self): 
        return print("Multiplication of x and y:", self.x*self.y)

    def division(self):
        return print("Division of x and y:", self.x/self.y)


my_calc_1 = MyCalculation(3, 5)
my_calc_1.addition()
my_calc_1.subtraction()
my_calc_1.multiplication()
my_calc_1.division()