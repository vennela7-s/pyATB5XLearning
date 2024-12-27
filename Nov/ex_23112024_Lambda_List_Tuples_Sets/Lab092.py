def find_even_odd(num):
    if num%2==0:
        print("even:",num)
    else:
        print("odd:", num)

find_even_odd(5)

n = int(input("Enter num"))
res = lambda n:"Even" if n%2==0 else "Odd"
print(res(7))
print(res(n))