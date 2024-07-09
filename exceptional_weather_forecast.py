# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating 
# a weather forecast application that gracefully handles unexpected user input and provides user-friendly 
# error messages.

# Task 1: Start 
# Begin by asking the user to enter the temperature in Fahrenheit.

input = int(input("What is the temparature, in Fahrenheit?"))


# Task 2: Temperature Conversion 
# Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit_temperature = 90.5
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is {celsius_temperature} degrees Celsius.")

# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?

def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ValueError:
        return "Invalid input: Please enter a numerical value."

print(fahrenheit_to_celsius(30))
print(fahrenheit_to_celsius("thirty"))

# Task 3: User Experience 
# Implement an else block that prints the converted temperature in a user-friendly format. 

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    if celsius < 1:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius. It is freezing!")
    elif 0 <= celsius <= 25:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius. It is comfortable temperature.")
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:2f} degrees Celsius. It is quite hot!")

fahrenheit_to_celsius(32)
fahrenheit_to_celsius(68)
fahrenheit_to_celsius(100)

# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

# Task 4: Finally 
# Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

def fahreinheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        print("Thank you for using the weather forecast application.")

fahrenheit = 90.5
celsius = fahrenheit_to_celsius(fahrenheit)

print("Thank you for using the weather forecast application.")
