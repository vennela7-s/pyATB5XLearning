# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))


def sum_of_num(num1=100, num2=200, num3=300):  # default values here
    return num1 + num2 + num3


result = sum_of_num(num1, num2, num3)
print(result)
result = sum_of_num(10)
print(result)
result2 = sum_of_num()
print(result2)
result2 = sum_of_num(10, 10)
print(result2)
