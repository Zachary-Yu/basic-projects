weight = input("Enter your weight: ")
while not weight.isdecimal():
    print(f"{weight} is invalid. Please enter a number.")
    weight = input("Enter your weight: ")
    
    
weight = float(weight)

unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Kgs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Lbs"
else:
    print(f"{unit} was not valid.")
    unit = input("Kilograms or Pounds? (Kgs or Lbs): ")
    
print(f"Your weight is {round(weight, 1)} {unit}.")
    
    