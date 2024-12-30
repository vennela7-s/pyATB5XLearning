# Sort a dictionary by its values in ascending order
#my_dict = {"a": 3, "b": 1, "c": 2}
from audioop import reverse

# {b: 1 , c: 2 , a :3}
from audioop import reverse
my_dict = {"a": 3, "b": 1, "c": 2}
sorted_dict = dict(sorted(my_dict.items(),key= lambda item:item[1]))
print(sorted_dict)
sorted_dict_desc = dict(sorted(my_dict.items(), key = lambda  item: item[1], reverse= True))
print(sorted_dict_desc)
