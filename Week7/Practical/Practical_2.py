# Ստեղծեք Car class-ը, որն ունի հետևյալ attribute-ները՝ model, color և max_speed։
# Ստեղծեք compareCar(self, car2) մեթոդը, որը ստանում է ևս մեկ Car տիպի object
# որպես argument ու կվերադարձնում է “car1 is better than car2” եթե ձեր մեքենայի
# maxSpeed attribute-ի արժեքը մեծ է car2-ի maxSpeed attribute-ի արժեքից և “car2 is
# better than car1”՝ հակառակ դեպքում։
# Փորձարկեք class-ի աշխատանքը ստեղծելով այդ class-ի object(ներ)։

class Car: 
    def __init__(self, model, color, max_speed): 
        self.model = model
        self.color = color
        self.max_speed = max_speed
      
    def compareCar(self, car2): 
        if self.max_speed > car2.max_speed: 
            return print("car1 is better than car2")
        else: 
            return print("car2 is better than car1")


car1 = Car("BMW", "black", 250)
car2 = Car("Mercedez", "white", 270)

car1.compareCar(car2)
