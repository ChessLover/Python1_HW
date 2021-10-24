# Ստեղծեք Circle class-ը, որն ունի հետևյալ attribute-ները՝ radius և color։ Class-ի
# ներսում ստեղծեք getDesc(self) մեթոդը, որը կտպի “A color circle with radius
# radius.” ՝ օգտագործելով համապատասխան attribute-ների արժեքները։
# Փորձարկեք class-ի աշխատանքը ստեղծելով այդ class-ի object(ներ)։


class Circle: 
    def __init__(self, color, radius): 
        self.radius = radius
        self.color = color
      
    def getDesc(self): 
        return print("A %s circle with radius %d." %(self.color, self.radius))
    


c1 = Circle("blue", 15)
c2 = Circle("red", 2)

c1.getDesc()
c2.getDesc()