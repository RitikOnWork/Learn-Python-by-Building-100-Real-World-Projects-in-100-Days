# Number Comparison Tool

# Step 1: Get user input of 2 Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2 : Compare the numbers using if-else statements
print("Comparing the two numbers...")

if num1 == num2:
    print(f"Both numbers are equal.{num1}")
elif num1 > num2:
    print(f"The first number ({num1}) is greater than the second number ({num2}).")
else:
    print(f"The second number ({num2}) is greater than the first number ({num1}).")

# Step 3: Check if any number is zero
if num1 == 0 or num2 == 0:
    print("One of the numbers is zero.")
else:
    print("Neither number is zero.")
