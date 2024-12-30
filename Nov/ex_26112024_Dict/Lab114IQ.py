input_string = "Hello, World!"
a = input_string.lower()
# print(a)
vowels = "aeiou"
count = 0
new = 0
for char in a:
    if char in vowels:
        count += 1
    else:
        new += 1
print(count)
print(new)
