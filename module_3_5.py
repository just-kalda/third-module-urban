def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0: # В задании вывод выглядит как 24 и 24 - для этого добавил проверку на 0 в конце, иначе получается 24 и 0
        return 1
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
        
        
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
