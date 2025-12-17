# Safe Calculator with Exception Handling
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result
    
# Example usage
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed.
print(safe_divide(10, 'a'))  # Output: Error: Invalid input
# type. Please provide numbers.
print(safe_divide(15, 3))  # Output: 5.0
print(safe_divide(7, -1))  # Output: -7.0
print(safe_divide(5, 2.5))  # Output: 2.0
print(safe_divide('x', 2))  # Output: Error: Invalid input type. Please provide numbers.
print(safe_divide(0, 5))  # Output: 0.0
print(safe_divide(100, 20))  # Output: 5.0
print(safe_divide(9, 3))  # Output: 3.0
print(safe_divide(8, 0))  # Output: Error: Division by zero is not allowed.
print(safe_divide(4, 2))  # Output: 2.0
print(safe_divide(6, 'b'))  # Output: Error: Invalid input type. Please provide numbers.
print(safe_divide(12, 4))  # Output: 3.0