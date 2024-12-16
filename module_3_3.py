def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)


print_params()
print_params(5, {0, "Строка"})
print_params(10, "1", 19.72)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, False, []]
values_dict = {"a": "Строка", "b": 99, "c": 12.1}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)
