num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if num1 >= num2 and num1 >= num3:
    print("max is num1", num1)
elif num2 > num3 and num2 > num1:
    print("max is num2", num2)
else:
    print("max is num3", num3)