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



# Задание 5
# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне от 0 до 6 нужно вывести надпись Good Night,
# если в диапазоне от 6 до 13 Good Morning,
# если в диапазоне от 13 до 17 Good Day, если в диапазоне от 17 до 0 Good Evening.
# Верхняя граница диапазона не включается. Например, число 6 относится к 6 до 13