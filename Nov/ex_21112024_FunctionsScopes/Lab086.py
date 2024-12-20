import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Start Time: {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"End Time: {end_time}")
        print("Total Time Taken by Function ->", end_time - start_time)
        return result
    wrapper()
    return wrapper


def print_logs(func):
    def wrapper(*args, **kwargs):
        print("Starting log")
        result = func(*args, **kwargs)
        print("Ending log")
        return result
    wrapper()
    return wrapper


@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)


@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)


# Testing the functions
#test_ui_1()
#test_ui_2()
