class PyATB:
    def __init__(self,name,age,gender,occupation,id):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.id = id
    def student1_info(self):
        return self.name,self.age,self.gender,self.occupation,self.id
    def stud2_info(self):
        return self.name, self.age, self.gender, self.occupation, self.id
    def stud3_info(self):
        return self.name, self.age, self.gender, self.occupation, self.id
obj1 = PyATB("Vennela",25,"Female","Test Automation Engineer", 2123)
obj2 = PyATB("John",28,"Male","Test Automation Engineer", 2123)
obj3 = PyATB("Thomas",52,"Male","Test Automation Engineer", 2123)

output_stud_info = obj1.student1_info()
output_stud2_info = obj2.stud2_info()
output_stud3_info = obj3.stud3_info()
print(output_stud_info,output_stud2_info,output_stud3_info)