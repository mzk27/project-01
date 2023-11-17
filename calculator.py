# calculator.py

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of the input integer.
        
    Raises:
        ValueError: If the input is a negative number.
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative values")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the n-th number.

    Parameters:
        n (int): Number of Fibonacci numbers to generate.

    Returns:
        str: Comma-separated string of Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_string = ", ".join(map(str, fib_sequence))
    return fib_string