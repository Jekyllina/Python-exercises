import pytest

from circle import Circle

def test_circle_init():
    circle = Circle(radius=10)
    circle2 = Circle(diameter=5)
    
    assert circle.radius == 10
    assert circle.diameter == 20
    assert circle.area == 314.15926535897932384626433832795
    
    assert circle2.radius == 2.5
    assert circle2.diameter == 5
    assert circle2.area == 19.634954084936207740391521145497

def test_circle_str():    
    circle = Circle(radius = 4)
    assert str(circle) == "Circle radius: 4, Circle diameter: 8, Circle area: 50.265" 

def test_circle_add(): 
    circle = Circle(radius=2)
    circle2 = Circle(diameter=3)

    circle_add = circle + circle2

    assert circle_add.radius == 3.5
    assert circle_add.diameter == 7
   
def test_circle_eq(): 
    circle = Circle(radius=2)
    circle2 = Circle(diameter=4)

    assert circle == circle2

def test_circle_lt(): 
    circle = Circle(radius=8)
    circle2 = Circle(radius = 6)

    assert circle2 < circle

def test_circle_gt(): 
    circle = Circle(radius=1)
    circle2 = Circle(radius = 7)

    assert circle2 > circle

def test_circles_sort():
    circle = Circle(radius=2)
    circle2 = Circle(radius = 7)
    circle3 = Circle(radius = 4)

    circles = []
    circles.append(circle)
    circles.append(circle2)
    circles.append(circle3)

    circles.sort(key=lambda x : x.area)

    assert circles[0].radius == 2
    assert circles[1].radius == 4
    assert circles[2].radius == 7