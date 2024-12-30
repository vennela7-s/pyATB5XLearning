# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}
my_dict = {"a": 10, "b": 20, "c": 30}
my_values_list = []
for key, value in my_dict.items():
    my_values_list.append(value)
    # print(new_values)
    # print(value)
print(my_values_list)
print(max(my_values_list))


def max_min_value(my_dict):
    max_value = max(my_dict.values())
    min_value = min(my_dict.values())
    return min_value,max_value


my_dict = {"a": 10, "b": 20, "c": 30}
result = max_min_value(my_dict)
print(result)
