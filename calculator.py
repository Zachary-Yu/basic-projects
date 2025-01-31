# First number
num = input("Enter your first number: ")
while not num.isdecimal():
    print("Invalid input. Please enter a decimal number.")
    num = input("Enter your first number: ")
# Ensuring num is an integer
num = float(num)

# Second number
num2 = input("Enter your second number: ")
while not num2.isdecimal():
    print("Invalid input. Please enter a decimal number.")
    num2 = input("Enter your second number: ")
# Ensuring num2 is an integer
num2 = float(num2)
    
# Choose operator   
operator = input("Enter an operator: (+ - x /): ")

# Addition
if operator == '+':
    result = num + num2
    print(f"The sum of {num} and {num2} is {round(result, 3)}.")
    
# Subtraction
elif operator == '-':
    result = num - num2
    print(f"The difference between {num} and {num2} is {round(result, 3)}.")
    
# Multiplication
elif operator == "x":
    result = num * num2
    print(f"The product of {num} and {num2} is {round(result, 3)}.")
    
# Division
elif operator == "/":
    result = num / num2
    print(f"The quotient of {num} divided by {num2} is {round(result, 3)}.")
    
else:
    print("Invalid operator. Please choose from +, -, x, or /.")