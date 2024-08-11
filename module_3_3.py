def print_params(a = 1, b = 'строка', c = True):
    print(f"a = {a}, b = {b}, c = {c}")

# Вызов функции с разными количествами аргументов
print_params()  # Без аргументов
print_params(10, 'новая строка', False)  # С новыми значениями
print_params(b = 25)  # С одним аргументом
print_params(c = [1,2,3])  # С одним аргументом

# Распаковка параметров
values_list = ['строка', 10, False]
values_dict = {'a': 'строка', 'b': 10, 'c': False}
print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка списка и отдельный параметр