# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# Пример: 1, 2, 5, 2, 5 => 1


# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. 
# Приотритет операций стандартный.

# data = '-1+2-3*7/4'

# data = data.replace('-', ' -').replace('+', ' ').replace('*', ' * ').replace('/', ' / ')
# data = data.split()

# for i in range(len(data)):
#     try:
#         data[i] = int(data[i])
#     except:
#         continue



# for i in range(len(data)):
#     if data[i] == '*':
#         data[i] = 0   
#         data[i+1] = data[i-1] * data[i+1]  
#         data[i-1] = 0  
#     elif data[i] == '/':
#         data[i] = 0   
#         data[i+1] = data[i-1] / data[i+1]  
#         data[i-1] = 0

# print(sum(data))

data_1 = '-45*(23*34-32-23)/ (24*3*4*3-7*4)+3-9*2*(2-4+71/4)'
print(data_1)

data_1 = data_1.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')\
        .replace('(', ' ( ').replace(')', ' ) ')
data_1 = data_1.split()

for i in range(len(data_1)):
    try:
        data_1[i] = float(data_1[i])
    except:
        continue

def multiplication_and_division_with_parenthesis(data, i):
    for i in range(i, len(data)):
        if data[i] == ')':
            break
        else:
            if data[i] == '*':
                data[i] = 0   
                data[i+1] = data[i-1] * data[i+1]  
                data[i-1] = 0

            elif data[i] == '/':
                data[i] = 0   
                data[i+1] = data[i-1] / data[i+1]  
                data[i-1] = 0
    return data

def addition_and_subtraction_with_parenthesis(data, i):
    for i in range(i, len(data)):
        if data[i] == ')':
            break
        else:
            if data[i] == '+':
                data[i] = 0   
                data[i+1] = data[i-1] + data[i+1]  
                data[i-1] = 0

            elif data[i] == '-':
                data[i] = 0   
                data[i+1] = data[i-1] - data[i+1]  
                data[i-1] = 0
    return data

def multiplication_and_division(data):
    for i in range(len(data)):
        if data[i] == '*':
            if data[i+1] == '(' or data[i+1] == ')' or data[i-1] == '(' or data[i-1] == ')':
                continue
            else:        
                data[i] = 0   
                data[i+1] = data[i-1] * data[i+1]  
                data[i-1] = 0

        elif data[i] == '/':
            if data[i+1] == '(' or data[i+1] == ')' or data[i-1] == '(' or data[i-1] == ')':
                continue
            else:   
                data[i] = 0   
                data[i+1] = data[i-1] / data[i+1]  
                data[i-1] = 0
    return data

for i in range(len(data_1)):
    if data_1[i] == '(':
        multiplication_and_division_with_parenthesis(data_1, i + 1)
data_2 =[]
for i in range(len(data_1)):
    if not data_1[i] == 0:
        data_2.append(data_1[i])

for i in range(len(data_2)):
    if data_2[i] == '(':
        addition_and_subtraction_with_parenthesis(data_2, i + 1)

data_2 = multiplication_and_division(data_2)

data_3 = []
for i in range(len(data_2)):
    if not data_2[i] == 0 and not data_2[i] == '(' and not data_2[i] == ')':
        data_3.append(data_2[i])

for i in range(len(data_3)):
    if data_3[i-1] == '-':
        data_3[i] *= -1

data_1 = []
for i in range(len(data_3)):
    if not data_3[i] == 0:
        data_1.append(data_3[i])

data_1 = multiplication_and_division_with_parenthesis(data_1, 1)
data_1 = [item for item in data_1 if not item == '-' and not item == '+']

print(round(sum(data_1),2))

