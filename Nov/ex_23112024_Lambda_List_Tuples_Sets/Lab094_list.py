# List - Collection  of items
# grocery List -  butter, bread, banana, paneer.
# 10th marks - 90,91,92, 78, 56
#mutable we can add or remove

my_list = [1, 2, 3]  # Same type of data (int)
my_list2 = [1, True, "string", 12.34]
# duplicates are allowed in list
print(my_list)
print(len(my_list2))
my_list[0] = "Hi"
my_list[1] = "hello"
my_list[2] = 1
print(my_list)
for item in my_list2:
    print(item)
for i in range(1, 5):
    print(i, end=" ")
