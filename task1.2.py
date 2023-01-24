# Задайте список из n чисел последовательности (1 + 1/n)^n, 
# выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# def input_int():
#     is_ok = False
#     while is_ok != True:
#         try:
#             number = int(input('Input a number: '))
#             if number > 0:
#                 is_ok = True
#             else:
#                 print('Incorrect a number')
#         except ValueError:
#             print('Its not a correct number')
#     return number

# n = input_int()

# my_list = []
# my_sum = 0

# for i in range(n):
#     my_list.append((1 + 1/(i + 1))**(i + 1))
#     my_list[i] = round(my_list[i], 2)
#     my_sum += my_list[i]

# print(f'The list: {my_list}')
# print(f'Sum is {my_sum}')

def input_int():
    while True:
        try:
            number = int(input('Input a number: '))
            if number > 0:
                break
            else:
                print('Incorrect a number')
        except ValueError:
            print('Its not a number')
    return number

n = input_int()
my_list =  [_ for _ in range(n)]
my_list = list(map(lambda x: round((1 + 1/(x + 1))**(x + 1), 2), my_list))
print(my_list, sum(my_list))

