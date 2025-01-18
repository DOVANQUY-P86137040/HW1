def add_numbers(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.

    Example:
        >>> add_numbers(1, 2)
        3
        >>> add_numbers(-1, 1)
        0
    """
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
