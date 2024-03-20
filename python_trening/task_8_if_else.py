# 1
num = -1
if num >= 0:
    print('Чистло больше либо равно 0')
else:
    print('Число отрицательное')
#2
str_1 = 'test1'
str_2 = 'test'
if str_2 == str_1:
    print('Да')
else:
    print('Нет')

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('Да')
    else:
        print('Нет')
task_yes_no(str_1 = 'test', str_2 = 'test1')

# 3
num_float = 3.4
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

# 4
permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

# 5
def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Бакалавр')
    elif year_of_study == 5 or year_of_study == 6:
        print('Магистр')
    elif year_of_study == 7 or year_of_study == 8 or year_of_study == 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')
student_rank(11)

def student_rank(year_of_study):# Аналог решения придыдущей задачи
    if year_of_study in range(1, 5):
        print('Бакалавр')
    elif year_of_study in range(5, 7):
        print('Магистр')
    elif year_of_study in range(7, 10):
        print('Аспирант')
    else:
        print('Введите корректный год обучения')
student_rank(7)

# 6
def nuber_1(a):
    if a > 100 or a < -100:
        print('-')
    else:
        print('+')
nuber_1(500)
# Альтернативное решение предыдущей задачи
a = 10
if a > 100 or a < -100:
    print('-')
else:
    print('+')

