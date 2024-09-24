FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):

    celsius = (fahrenheit  - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

def convert_to_fahrenheit(celsius):

    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

user_temperature = input(f"Enter the temperature to convert: ")


temperature_unit = input(f"Is this temperature in Celsius or Fahrenheit? (C/F): ")

if user_temperature.isdigit():
    
    user_temperature = float(user_temperature)

    if temperature_unit.upper() == "F":
        
        celsius = convert_to_celsius(user_temperature)
        
        print(f"{user_temperature}°F is {celsius}°C")
        
    elif temperature_unit.upper() == "C":
        
        fahrenheit = convert_to_fahrenheit(user_temperature)
        
        print(f"{user_temperature}°C is {fahrenheit}°F")
        
    else:
        print(f"{temperature_unit} unit is not valid")
        
else:
    print(f"Invalid temperature. Please enter a numeric value. ")
    


