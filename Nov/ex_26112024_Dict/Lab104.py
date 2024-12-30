my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "experience": 3
}
print(my_dict)
print(my_dict["age"])
my_dict["name"] = "Vennela"
print(my_dict["name"])
print(my_dict)
#del my_dict["role"]
#print(my_dict)
for key, value in my_dict.items():
    print(key, "----->>>", value)
    