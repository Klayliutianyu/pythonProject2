"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4
print("{} {} for about ${:,.0f}！".format(year, name, cost))
print()
numbers = {0, 50, 100, 150}
for number in numbers:
    print("{:>3}".format(number))
