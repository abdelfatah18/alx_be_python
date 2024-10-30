# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using a global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using a global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

