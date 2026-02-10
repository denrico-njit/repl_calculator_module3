def addition(a: float, b: float) -> float:
    """
    Returns the sum of a and b.
    """
    return a + b  

def subtraction(a: float, b: float) -> float:
    """
    Returns the signed difference of a and b. i.e. a - b
    """
    return a - b  

def multiplication(a: float, b: float) -> float:
    """
    Returns the product of a and b
    """
    return a * b  # This multiplies the two numbers and returns the result.

def division(a: float, b: float) -> float:
    """
    Returns a divided by b. B cannot be zero, or else a ValueError will be returned.
    """
    if b == 0:
        raise ValueError("Division by zero is undefined.\n")  
    return a / b 
