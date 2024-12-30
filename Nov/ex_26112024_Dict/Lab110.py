dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}
missing_keys1 = set(dict1.keys())
missing_keys2 = set(dict2.keys())
print(missing_keys1)
print(missing_keys2)
missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)

# Sort a dictionary by its values in descending order
my_dict1 = {"a": 3, "b": 1, "c": 2}
sorted_by_keys1 = dict(sorted(my_dict1.items()))
sorted_by_values = dict(sorted(my_dict1.items(), key=lambda item: item[1]))
print(sorted_by_values)
print(sorted_by_keys1)

my_dict = {'b': 2, 'a': 3, 'c': 1}
sorted_by_keys = dict(sorted(my_dict.items()))
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print(sorted_by_keys_desc)
print(sorted_by_values)
print(sorted_by_keys)

# {b: 1 , c: 2 , a :3}
