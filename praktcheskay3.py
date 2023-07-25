# Задание 1
# Показать на экран все простые числа в диапазоне, указанном пользователем.
# Число называется простым, если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

a = int(input("Введите число: "))
b = int(input("Введите число: "))

for d in range(a,b):
    c = 0
    for x in range(2, d +1):
        if d % x == 0:
            c = c+1
    if c <= 2:
        print(d)

# Задание 2
# Показать на экране таблицу умножения для всех чисел от 1 до 10. Например:
# 1 * 1 = 1 1 * 2 = 2 ..... 1 * 10 = 10
# .........................................................................
# 10 * 1 = 10 10 * 2 = 20 .... 10 * 10 = 100.
for x in range(1, 10+1):
    for y in range(1, 10+1):
        print(x, "x", y, "=", x*y, end="\t ") # выводим строку
    print('\n', '.'*120, sep='') # выводим перенос строки, 120 шт точек,
                                 # разделитель чтоб точки начинались с начала строки


# Задание 3
# Показать на экран таблицу умножения в диапазоне, указанном пользователем. Например, если пользователь указал 3 и 5, таблица может выглядеть так
# 3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
# .....................................................................................
# 5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50
# a = int(input("Введите число:"))
# b = int(input("Введите число:"))
for x in range(a, b+1):
    for y in range(1, 10+1):
        print(x, "x", y, "=", x*y, end="\t ") # выводим строку
    print('\n', '.'*120, sep='') # выводим перенос строки, 120 шт точек,
#                                  # разделитель чтоб точки начинались с начала строки

# Задание 1
# Пользователь вводит с клавиатуры размер стороны квадрата.
# Требуется отобразить на экран заполненный квадрат.
# Размер стороны равен введённому размеру.
# Например, если пользователь ввёл 3 на экране будет выведено:
# ***
# ***
# ***
a = int(input("Введите число:"))
for x in range(a):
    print('*'*a)
# Задание 2
# Пользователь вводит с клавиатуры ширину и высоту прямоугольника.
# Требуется отобразить на экран заполненный прямоугольник с указанными высотой и шириной.
# Например, если пользователь ввёл высоту 3, а ширину 5 на экране будет выведено:
#     *****
#     *****
#     *****
a = int(input("Введите ширину прямоугольника:"))
b = int(input("Введите высоту прямоугольника:"))
for x in range(a):
    for i in range(b):
        print('*',end="")
    print()