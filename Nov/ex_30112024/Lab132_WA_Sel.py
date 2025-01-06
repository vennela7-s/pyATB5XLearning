class VWOLoginPage:
    def __init__(self,email,password):
        self.email =email
        self.password = password
    def login_confirm(self):
        if self.email == "vsankend@gmail.com" and self.password == "Venni777":
            print("login success")
        else:
            print("enter the correct password or email")
email = input("Enter the email:\n")
password = input("Enter the password: \n")
vwol_obj = VWOLoginPage(email,password)
vwol_obj.login_confirm()