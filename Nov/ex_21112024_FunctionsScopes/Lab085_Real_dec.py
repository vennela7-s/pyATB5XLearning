import time


def time_dec(func):
    def wrapper():
        start_time = time.time()
        print(start_time, "1st")
        func()
        end_time = time.time()
        print(end_time, "2nd")
        print("Total time->", end_time - start_time)

    return wrapper()


@time_dec
def test_ui1():
    print("Add a function, time taken by this funcui1")
    #time.sleep(2)


@time_dec
def test_ui2():
    print("Add a function, time taken by this funcui2")
    #time.sleep(5)
