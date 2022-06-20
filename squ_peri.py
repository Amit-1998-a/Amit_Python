class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*(self.side)

#initialize the objects of Square class
square1 = Square(10)
square2 = Square(20)

print(square1.area())
print( square1.perimeter())

print( square2.area())
print(square2.perimeter())