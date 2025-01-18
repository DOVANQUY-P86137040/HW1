def calculate(a: float, b: float, operation: str) -> float:
    """
    Perform a basic mathematical operation (+, -, *, /) on two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.
        operation (str): The operation to perform ('+', '-', '*', '/').

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If an unsupported operation is provided.

    Example:
        >>> calculate(10, 5, '+')
        15.0
        >>> calculate(10, 5, '-')
        5.0
        >>> calculate(10, 5, '*')
        50.0
        >>> calculate(10, 5, '/')
        2.0
        >>> calculate(10, 0, '/')
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
