class Circle:
    pi=3.14
    def __init__(self, radius):
        self.radius=radius
    def Area(self):
        print("area of circle is"+ str(self.pi*self.radius*self.radius))
    def circumference(self):
        print("area of circle is"+ str(2*self.pi*self.radius))
Cic1=Circle(3)
Cic1.Area()
Cic1.circumference()