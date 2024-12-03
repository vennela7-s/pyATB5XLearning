def print_mul_args(*args):
    # *args->list
    for i in args:
        print(i)


print_mul_args("Vennela")
print_mul_args("Hi", "hello", "vens", "lucky")
print_mul_args("hi", 10, True, 2.6)

