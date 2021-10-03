"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
while denominator == 0:
    denominator = int(input("Enter the denominator: "))
    fracytion = numerator / denominator
try:
    fraction = numerator / denominator
    print(fraction)
except ZeroDivisionError:
    print("denminator cannot be zero")
except ValueError:
    print("Please end a valid integer")
