# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = float(input('Input a number: '))

# def input_float():
#     while True:
#         try:
#             number = float(input('Input a number: '))
#             break
#         except ValueError:
#             print('Its not a number')
#     return number


# def sum_of_number(number):

#     sum = 0

#     for i in str(abs(number)):
#         if i != '.':
#             sum += int(i)

#     return sum

# number = input_float()
# print(sum_of_number(number))

while True:
    try:
        number = float(input('Input a number: '))
        break
    except ValueError:
        print('Its not a number')

number = str(number).replace('', ' ').replace('.', '')
number = list(filter(lambda x: not x == ' ', number))
number = [int (x) for x in number]
print(sum(number))