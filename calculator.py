def main():
    
    print("Please choose one of the following:")
    print("-----------------------------------")
    print("1. Add numbers")
    print("2. Exit program")
    print("-----------------------------------")
    choice = input("")
    
    if choice == "1":
        add()
    elif choice == "2":
        print("Exiting the program...")
        exit()
    else:
        print("Please try again.")
        
    
        
def add():
    # First number
    num = input("Enter a number: ")
    while not num.isdecimal():
        print("Invalid input. Please enter a number.")
        num = input("Enter a number: ")
    # Ensuring num is a float
    num = float(num)

    # Second number
    num2 = input("Enter another number: ")
    while not num2.isdecimal():
        print("Invalid input. Please enter a number.")
        num2 = input("Enter another number: ")
    # Ensuring num2 is a float
    num2 = float(num2)

    calculate(num, num2)
    
def calculate(num, num2):     
    
    # Choose operator   
    operator = input("Enter an operator: (+ - x /): ")

    while operator != "+" and operator != "-" and operator != "x" and operator != "/":
        print("Invalid operator. Please try again and enter an appropriate operator.")
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
    
    
main()