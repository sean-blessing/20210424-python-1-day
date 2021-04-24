from circle import Circle

class Rectangle:
    """Rectangle class holds length and width attributes"""
    # above doctring is optional
    area_formula = "area = length * width"

    def __init__(self, length, width):
        pass
        self.length = length
        self.width = width

    def area(self):
        """ calculate the area for this rectangle """
        return self.length * self.width

rect_1 = Rectangle(5, 6)
rect_2 = Rectangle(10, 25)

print('rect_1 area: ', rect_1.area())
print('rect_2 area: ', rect_2.area())

circle_1 = Circle(3)
print('circle_1 area', circle_1.area())

print('circle_1 radius', circle_1.radius)

