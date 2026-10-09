"""
Main application module demonstrating utils functions.
"""

from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = float(input("Enter a number: "))
        
        sq_result = square(user_input)
        even_result = is_even(int(user_input))
        f_result = celsius_to_fahrenheit(user_input)
        
        print(f"\nResults for input: {user_input}")
        print(f"- Square: {sq_result}")
        print(f"- Even or Odd: {'Even' if even_result else 'Odd'}")
        print(f"- Temperature in Fahrenheit: {f_result:.2f}°F")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()