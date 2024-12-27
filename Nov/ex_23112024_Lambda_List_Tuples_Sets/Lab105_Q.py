# Find the first non-repeating character in a string using sets.

a = input()


def non_repeat(a):


    for char in a:
        if a.count(char) == 1:
            return char
    return None
res = non_repeat(a)
print(res)

