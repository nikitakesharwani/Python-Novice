from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__(self)

    @abstractmethod    
    def calcArea(self):
        pass

class circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return self.radius * self.radius * 3.14

class rectangle(GraphicShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calcArea(self):
        return self.length * self.breadth

c = circle(34)
print(c.calcArea())
r = rectangle(10 , 20)
print(r.calcArea())
        