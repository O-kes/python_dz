# Задание 1
# Два списка целых заполняются случайными числами. Необходимо:
num1 = [9, 5, 3, 8, 10]
num2 = [3, 6, 5, 7, 2]
# ■ Сформировать третий список,содержащий элементы обоих списков;

num3 = num1 + num2
print(num3)

# ■ Сформировать третий список, содержащий элементы обоих списков без повторений;

num3 = num1 + num2      #складываю 2 списка
#print(num3)             #чтоб видно было что было раньше
c = []                  # создаю переменную для записи туда новых значений
for x in num3:          # переменная x должна перебрать цифры в num3
    if x not in c:      # если x нет в списке
        c.append(x)     # добавляем x в с
print(c)

# ■ Сформировать третий список,содержащий элементы общие для двух списков;

num3 = num1 + num2
c = []
n =[]
for x in num3:
    if x not in c:
        c.append(x)
    else:
        n.append(x)
print(n)

# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;

# ■ Сформировать третий список, содержащий только минимальное и максимальное значение
# каждого из списков.

list = [min(num1), max(num1), min(num2),max(num2)]
print(list)



