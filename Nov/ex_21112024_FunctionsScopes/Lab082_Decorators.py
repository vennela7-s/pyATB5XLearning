def add_extra_security(func):

    def wrapper():
        print("Before the function is called")
        print("Add helmet, licence, dashcam, gloves.etc")
        func()
        print("After the function is called")
        print("Secure driving")

    return wrapper()


@add_extra_security
def drive_ev():
    print("Ola")

@add_extra_security
def drive_scooty():
    print("Normal Function")
    print("I am driving")