"""
Leap day occurs in each year that is a multiple of 4,
except for years evenly divisible by 100 but not by 400.
"""
year = int(input("year: "))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("Leap year")
else:
    print("Not a leap year")