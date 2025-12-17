# Temperature Converter with Return Values

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# Example usage
c_temp = 25
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C is {f_temp}°F")
f_temp = 77
c_temp = fahrenheit_to_celsius(f_temp)  
print(f"{f_temp}°F is {c_temp}°C")
