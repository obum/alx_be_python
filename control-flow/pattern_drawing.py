square_size = int(input("Enter the size of the pattern:"))

row_number = 0

while row_number < square_size:
    for mark in range(1, square_size+1):
        print("*", end="")
    print()
    row_number += 1
    