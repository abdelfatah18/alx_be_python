# temp_conversion_tool.py

# 1. Definition of Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Check: Global variable for Fahrenheit to Celsius factor
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Check: Global variable for Celsius to Fahrenheit factor

# 2. Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using a global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # Check: Uses global variable in conversion

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using a global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  # Check: Uses global variable in conversion

# 3. User Interaction and Input Validation
try:
    # User inputs temperature and unit
    temperature = float(input("Enter the temperature to convert: "))  # Check: Validates numeric input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Determines which conversion function to use based on unit
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")  # Check: Converts Fahrenheit to Celsius and outputs result
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")  # Check: Converts Celsius to Fahrenheit and outputs result
    else:
        # Raises ValueError for invalid unit input
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# 4. Implementation of Value Error Handling
except ValueError as e:
    print("Invalid temperature. Please enter a numeric value.")  # Check: ValueError handling for non-numeric input
    print(e)
