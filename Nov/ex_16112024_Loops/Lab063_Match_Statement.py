# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block


# Write a program to ask the user which browser he want to run automation.
browser_name = input("Enter the browser name: ")
match browser_name:
    case "firefox":
        print("starting firefox")
    case "chrome":
        print("Starting chrome")
    case "edge":
        print("Execute the edge")
    case _:
        print("browser not found")
#_ -> when nothing matches
