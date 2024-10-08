from math import pi

class Shape:
    def area(self):
        raise NotImplementedError(f'This method should be overridden by subclasses')
    
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

        
    def area(self):
        return pi * self.radius**2
    
    
# def main():
#     shapes: list[Shape] = [
#         Rectangle(10, 5),
#         Circle(7)
#     ]

#     for shape in shapes:
#         print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

# if __name__ == "__main__":
#     main()