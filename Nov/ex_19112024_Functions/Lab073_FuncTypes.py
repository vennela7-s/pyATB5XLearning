# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments
from Nov.ex_07112024_keywords_identifier_variables.Lab014_Math_Functions import result


# can't return -> non return
def greet():
    print("hello")


greet()


# no return type with argument/parameter
def greet_by_name(name):
    print("hello", name)


greet_by_name("Vennela")


def say_hello_default_arg(name="Vens"):
    print("Hello", name.upper())


say_hello_default_arg("Sann")
say_hello_default_arg()


def multiple_args(name1="A", name2="B"):
    print("multiple", name1, name2)


multiple_args()
multiple_args("Vens", name2="Amit")
multiple_args("Vennela")
multiple_args(name1="Vennela")
multiple_args("Vennela", "ma")


# Argument + return

def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 56)
print(result)


def sum_of_num_default(num1=100, num2=200):
    return num1 + num2


result = sum_of_num_default(34, 50)
print(result)
result = sum_of_num_default()
print(result)
