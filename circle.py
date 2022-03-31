import math

class Circle:
    def __init__(self, *, radius = None, diameter = None):
        if radius is not None:
            if radius <= 0:
                raise TypeError("Radius must be > 0")           

            self.radius = radius
            self.diameter = self.radius * 2
        elif diameter is not None:
            if diameter <= 0:
                raise TypeError("Diameter must be > 0") 

            self.diameter = diameter
            self.radius = self.diameter * 0.5
        elif radius is None and diameter is None:
            raise TypeError("Define a radius or a diameter for the circle")           

        self.area = math.pi * math.pow(self.radius, 2)

    #fare property con calcolo per diametro e area

    def __str__(self):
        return f"Circle radius: {self.radius}, Circle diameter: {self.diameter}, Circle area: {format(self.area, '.3f')}"

    def __add__(self, other):
        newCircle = Circle(radius = self.radius + other.radius, diameter = self.diameter + other.diameter)
        newCircle.area = self.area + other.area
        return newCircle

    def __eq__(self, other):
        return (self.area == other.area)

    def __lt__(self, other):
        return (self.area < other.area)

    def __gt__(self, other):
        return (self.area > other.area)  