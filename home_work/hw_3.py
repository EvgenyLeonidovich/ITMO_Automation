# Задача №1
def number(num_1, num_2):
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)


number(10, 20)


# Задача №2
def number(numb_1, numb_2):
    if numb_1 - numb_2 == 135 or numb_2 - numb_1 == 135:
        print('Yes')
    else:
        print('No')


number(135, 270)


# Задача №3
def month(a):
    if a in range(3, 6):
        print('Весна')
    elif a in range(6, 9):
        print('Лето')
    elif a in range(9, 12):
        print('Осень')
    elif a in range(1, 3) or a == 12:
        print('Зима')
    else:
        print('Введите корректный номер месяца')


month(13)


# Задача №4
def abc(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')


abc(11, 12, 15)

# Задача №5
list_0 = [1, 2, -3, 4, 5]
count = 0
for i in list_0:
    if i > 0:
        count += 1
print(count)

# Задача №6
years = 5
month = 7
print(((5*12) + 7) * 29)
