class Calculator:

    # addition
    def add(self, a, b):
        return a + b

    # subtraction
    def subtract(self, a, b):
        return a - b
    
    # mutltiplication
    def multiply(self, a, b):
        return a * b

    # division
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

# check your code
c = Calculator()
print(c.add(2, 3))      # Output: 5
print(c.subtract(5, 2)) # Output: 3
print(c.multiply(4, 6)) # Output: 24
print(c.divide(8, 4))   # Output: 2.0
print(c.divide(8, 0))   # Raises a ValueError with message "Cannot divide by zero!"

