from unittest import result


num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")

num1 = int(num1)
num2 = int(num2)

match operation:
    
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")

    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
        
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
        
    case "/":
        if num2 == 0:
            print(f"The result is approaching infinity because the second number is 0.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")