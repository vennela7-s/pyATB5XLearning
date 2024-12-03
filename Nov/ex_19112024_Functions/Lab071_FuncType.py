from Nov.ex_19112024_Functions.Lab066 import greet


def say_hello():
    print("hello")


say_hello()


# functions with argument, parameters

def greet_by_name(name):
    print("hello", name)
    print(f"Hello {name}")


greet_by_name("Vennela")
greet_by_name(123)
