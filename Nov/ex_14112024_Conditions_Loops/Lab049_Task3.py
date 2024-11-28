"""
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""
a = int(input("Side1: "))
b = int(input("Side2: "))
c = int(input("Side3: "))
if a==b==c:
    print("Equilateral Traingle")
elif a==b or b==c:
    print("Isosceles Traingle")
else:
    print("Scalene Triangle")