class Calculator:
    """
    Calculator class demonstrating static and class methods.
    """
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to calculate the sum of two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method to calculate the product of two numbers.
        Prints the calculation type from the class attribute.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
