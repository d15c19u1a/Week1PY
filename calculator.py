# Basic Calculator Program that performs basic mathematical operations based on user input.

# Ask user for the first number and convert their input to float
num_one = float(input("Type the first number: "))

# Ask user for the second number and convert their input to float
num_two = float(input("Type the second number: "))

# Ask user for the operation they want to perform and convert their input to lowercase
operation = input("Type ONE of the below mathematical operations.\n'addition', 'subtraction', 'multiplication', or 'division': ").lower()

# Initialize operator and result variables
operator = ""
result = None

# Perform the selected operation
if operation == "addition":
    operator = "+"
    result = num_one + num_two
elif operation == "subtraction":
    operator = "-"
    result = num_one - num_two
elif operation == "multiplication":
    operator = "*"
    result = num_one * num_two
elif operation == "division":
    operator = "/"
    if num_two != 0:
        result = num_one / num_two
    else:
        result = "You cannot divide by zero!"
else:
    result = "Invalid operation. Please choose 'addition', 'subtraction', 'multiplication', or 'division'."

# Display the operation and the result

# Check if result is a number (int or float)
if isinstance(result, (int, float)):
    # If it is, it prints the full mathematical equation.
    print(f"{num_one} {operator} {num_two} = {result}")
# If it is not a number, it prints the message without trying to show the equation, which avoids errors like referencing an undefined operator.
else:
    print(result)
