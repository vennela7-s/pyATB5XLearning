my_list = [1, 2, 3]

# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])
my_list.append(1)
my_list.append(5)
print(my_list)

my_list.extend([7, 8, 10, 9])
print(my_list)

# insert()
my_list.insert(1, "Dutta")
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)

my_list[1] = "Amit"
print(my_list)

# remove()
my_list.remove("Amit")
print(my_list)

print(" --------------------------")
print(" --------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list,"my copylist")

my_copy_list.remove("Dutta")
my_list.remove("Dutta")

#my_copy_list.sort()

print(my_list)
print(my_copy_list)
my_copy_list.sort()
print(my_copy_list,"sorted")


