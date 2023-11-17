from calculator import factorial

def test_factorial():
    # Test factorial of 0 and 1
    assert factorial(0) == 1
    assert factorial(1) == 1

    # Test factorial of a positive number
    assert factorial(5) == 120

    # Test factorial of a larger number
    assert factorial(10) == 3628800

    # Test factorial of a negative number (should raise ValueError)
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "Factorial undefined for negative values"