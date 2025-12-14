import math

class Shape:
    """
    Base class for all shapes.
    Defines the interface for area calculation.
    """
    def area(self) -> float:
        """
        Calculate the area of the shape.
        Must be overridden by derived classes.
        
        Returns:
            float: Area of the shape
        Raises:
            NotImplementedError: If the method is not overridden
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """
    Rectangle shape class, inherits from Shape.
    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: Area = length * width
        """
        return self.length * self.width


class Circle(Shape):
    """
    Circle shape class, inherits from Shape.
    Attributes:
        radius (float): The radius of the circle
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            float: Area = π * radius^2
        """
        return math.pi * self.radius ** 2
