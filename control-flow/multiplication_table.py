number = input("Enter a number to see its multiplication table:")

number = int(number)

for num in range(1, 11):
    print(f"{number} * {num} = {number*num}")