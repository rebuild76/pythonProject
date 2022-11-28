from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

#print(rect_1.getArea())
#print(rect_2.getArea())

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(13)
circle_2 = Circle(25)
#print(square_1.get_area_square())
#print(square_2.get_area_square())



figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for fig in figures:
    if isinstance(fig, Square):
        print(fig.get_area_square())
    elif isinstance(fig, Circle):
        print(fig.get_circle_area())
    else:
        print(fig.getArea())