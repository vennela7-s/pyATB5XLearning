from Nov.ex_19112024_Functions.Lab074_IQ import result2


def sum_of_three(a=1, b=1, c=1):
    return a + b + c


result = sum_of_three()
print(result)
result1 = sum_of_three(1, 2)
print(result1)
result2 = sum_of_three(1, 2, 3)
print(result2)
result3 = sum_of_three(c=10, b=1, a=2)
print(result3)
