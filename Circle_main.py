from circle import Circle

if __name__ == "__main__":
    circles = []
    circle = Circle(radius = -4)    
    print(str(circle))
    circles.append(circle)

    circle2 = Circle(radius = 2.5)
    print(str(circle2))
    circles.append(circle2)

    circleAdd = circle + circle2
    print(f"Sum of two circles: {str(circleAdd)}")

    print(f"The Circles are equals? {circle == circle2}")
    
    print(f"circle with area {circle.area} is bigger than circle2 with area {circle2.area}? {circle > circle2}")

    circle3 = Circle(diameter = 2)
    circles.append(circle3)

    circle4 = Circle(radius = 7)
    circles.append(circle4)

    circle5 = Circle(diameter = 6)
    circles.append(circle5)

    circles.sort(key=lambda x : x.area)

    print("\nCircles after sorting:")
    for circle in circles:
        print(str(circle)) 