def add_before_ui_after_ui(func):
    def wrapper():
        print("before running the UI TC")
        print("Start browser")
        func()
        print("Exit running the UI TC")
        print("Quit browser!")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("will test the UI")
