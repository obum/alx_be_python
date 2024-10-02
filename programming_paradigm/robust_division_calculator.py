
def safe_divide(numerator, denominator):
    try:
        answer = float(numerator) / float(denominator)
        
    except ZeroDivisionError:
        return(f"Error: Cannot divide by zero.")
        
    except ValueError:
        return(f'Error: Please enter numeric values only.')
        
    else:
        return(f'The result of the division is {answer}')