# Ստեղծեք My_Time class-ը:
# Attributes: t (str, ցույց է տալիս ժամանակ, օրինակ՝ “10 AM”)
# Methods: __init__(self, t) -> ստեղծում է t attribute
# printTime(self) -> տպում է “The current time is X”, X-ի փոխարեն օգտագործելով t attribute-ի
# արժեքը
# Ստեղծեք My_Date class-ը:
# Attributes: d (str, ցույց է տալիս ամսաթիվ, օրինակ՝ “12.02.2018”)
# Methods: __init__(self, d) -> ստեղծում է d attribute
# printDate(self) -> տպում է “The current date is Y”, Y-ի փոխարեն օգտագործելով d attribute-ի
# արժեքը
# Ստեղծեք Date_Time class-ը, որը ժառանգում է My_Date ու My_Time class-ներից:
# Attributes: d, t
# Methods: __init__(self, d, t) -> կանչում է My_Date class-ի __init__ method-ը d attribute-ով
# ու My_Time class-ի __init__ method-ը t attribute-ով
# Ստեղծեք Date-Time class-ի object “12 PM” ու “13.03.2013” attribute-ների արժեքներով ու
# կանչեք իր վրա printTime ու printDate method-ները:


class My_Time():
    def __init__(self, t): 
        self.t = t
        
    def printTime(self):
        return print("The current time is: ", self.t)
    
    
class My_Date(): 
    def __init__(self, d): 
        self.d = d
        
    def printDate(self):
        return print("The current date is: ", self.d)    


class DateTime(My_Time, My_Date): 
    def __init__(self, t, d):
        My_Time.__init__(self, t)
        My_Date.__init__(self, d)
        
    

dt = DateTime( "4:47 PM", "07.11.2021")
dt.printTime()
dt.printDate()