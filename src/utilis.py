"""
Utility functions for arithmetic and unit conversions.
"""

def square(n):
    """Returns the square of a number."""
    return n ** 2

def is_even(n):
    """Returns True if a number is even, False otherwise."""
    return n % 2 == 0

def celsius_to_fahrenheit(c):
    """Converts Celsius temperature to Fahrenheit."""
    return (c * 9 / 5) + 32