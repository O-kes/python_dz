# Задание 1
# Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность.
# Если число четное требуется вывести на экран число и надпись Even number.
# Если число нечетное выведите на экран число и надпись Odd number.
a = int(input("Введите число"))
if a/2 == 0:
    print(a,"Even number")
else:
    print(a,"Odd number")

# Задание 2
# Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7.
# Если число кратно требуется вывести на экран число и надпись Number is multiple 7.
# Если число не кратно выведите на экран число и надпись Number is not multiple 7.
a = int(input("Введите число"))
if a/7 == 1:
    print(a, "Number is multiple 7")
else:
    print(a, "Number is not multiple 7")

# Задание 3
# Пользователь вводит с клавиатуры два числа.
# Необходимо найти максимум из двух чисел и показать его на экран.

a = int(input('Введите первое число'))
b = int(input('Введите первое число'))

if a > b:
    print(a)
else:
    print(b)

# Задание 4
# Пользователь вводит с клавиатуры два числа.
# Необходимо найти минимум из двух чисел и показать его на экран.

a = int(input('Введите первое число'))
b = int(input('Введите первое число'))
print(min(a,b))



# Задание 5
# Пользователь вводит с клавиатуры два числа.
# В зависимости от выбора пользователя нужно показать сумму двух чисел,
# разницу двух чисел, среднеарифметическое или произведение двух чисел.
a = int(input('Введите первое число'))
b = int(input('Введите первое число'))
x = int(input("Напишите что хотите получить сумма 1, разница 2, средняя 3, произведение 4"))
sum = a + b
dif = a - b
sr = (a+b)/2
pr = a * b
if x == 1:
    print("Сумма чисел:", sum)
elif x == 2:
    print("Разница чисел:", dif)
elif x == 3:
    print("Средняя:", sr)
elif x == 4:
    print("Произведение чисел:", pr)

# Задание 1
# Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня.
# В зависимости от выбора пользователя посчитать, сколько часов, минут и секунд осталось до полуночи.
seconds = int(input("Введите количество секунд: "))
choice = input("Напишите Часы: Минуты: Секунды: Все: ")
hours = (86400 - seconds) // 3600  # Используем целочисленное деление иначе получается большой хвост
# Из общего числа секунд вычитаем кол-во введенных секунд и это число делим на 3600 сек(это один час)
# Получаем часы. и.т.д
minutes = (86400 - seconds) % 3600 // 60  # Из общего числа вычитаем введеное кол-во секунд, остаток преобразовываем в минуты
secondsv = (86400 - seconds) % 60
if choice == "Часы":
    print("Осталось", hours, "часов до полуночи")
elif choice == "Минуты":
    print("Осталось", minutes, "минут до полуночи")
elif choice == "Секунды":
    print("Осталось", secondsv, "секунд до полуночи")
elif choice == "Все":
    print("Осталось", hours, 'часа', minutes, 'минут', secondsv, 'секунд' " до полуночи")

# Задание 2
# Пользователь вводит с клавиатуры диаметр окружности.
# В зависимости от выбора пользователя посчитать площадь или периметр окружности.

d = int(input("Введите диаметр окружности"))
x = input("Напишите что посчитать: s или p ")
s = (d*d/4)*3.14
p = d * 3.14
if x == "s":
    print("площадь равна:",s)
elif x == "p":
    print("периметр:",p)

# Задание 3
# Пользователь вводит с клавиатуры стоимость одной игровой приставки, их количество и процент скидки.
# В зависимости от выбора пользователя посчитать общую сумму заказа или стоимость одной приставки с учетом скидки.

a = int(input('Стоимость одной приставки:'))
b= int(input('Количество:'))
c = int(input('скидка:'))
x = input('общую сумму заказа "введите 1, стоимость одной приставки с учетом скидки "введите 2')

s = a*b/100*c
o = a*b-s
o1 = a-c
if x == "1":
    print('общая сумма',o)
elif x == "2":
    print('стоимость одной с учетом скидки',o1)

# Задание 4
# Пользователь вводит с клавиатуры размер файла в гигабайтах и скорость интернет-соединения в битах в секунду.
# В зависимости от выбора пользователя посчитать, за сколько часов или минут, или секунд скачается файл.
# a = int(input('Введите размер файла в Гб:'))
# b = int(input('Введите сакорость интернет соединения в битах:'))
# x = input('За сколько часов:1, Минут:2, Секунд:3 ')
# g = 1073741824



