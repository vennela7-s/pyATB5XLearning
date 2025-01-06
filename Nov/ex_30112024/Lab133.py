from dotenv import load_dotenv
import os
class VWOLoginPage:
    def __init__(self,email,password):
        self.email =email
        self.password = password
    def login_confirm(self):
        if self.email == "vsankend@gmail.com" and self.password == "Pass@123":
            print("login success")
        else:
            print("enter the correct password or email")
load_dotenv()
email = os.getenv("email")
password = os.getenv("password")
vwol_obj = VWOLoginPage(email,password)
vwol_obj.login_confirm()
print(email,password)