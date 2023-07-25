# Задание 1
# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
#                      Steve Jobs
a = '“Don t let the noise of others opinions drown out your own inner voice.”Steve Jobs'
def my_text(a):
    print('Don t let the noise of others opinions \ndrown out your own inner voice.')
    print('\t'*7,'Steve Jobs')
my_text(a)

# Задание 2
# Напишите функцию, которая принимает два числа в качестве
# параметра и отображает все нечетные числа между ними.
# a = int(input('Введите начало диапазона:'))
# b = int(input('Введите конец диапазона:'))
def my_number(a,b):
    for num in range(a,b):
        if num % 2 == 1:
            print(num)
my_number(4,9)

# Задание 3
# # Напишите функцию, которая отображает горизонтальную или вертикальную линию из
# # некоторого символа.
# # Функция принимает в качестве параметра: длину линии, направление, символ.


def line (dlina, napravlenie, symvol):
    print(symvol * dlina, end=napravlenie)

line(5 ,'', '$')

# Задание 4
# Напишите функцию, которая возвращает максимальное из четырёх чисел.
# Числа передаются в качестве параметров.

def max_4_numbers(a, b, c, d):
    return max([a,b,c,d])
print(max_4_numbers(9, 20, 11, 5))

# Задание 5
# Напишите функцию, которая возвращает сумму чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров.

def sum_num(min_num, max_num):
    diapazon = sum(range(min_num,max_num))
    return diapazon
print(sum_num(1,4))
# За диапазон взяла от 1 до числа 4,то есть(1, 2 , 3 ) поэтому указывать +1 не стала

# Задание 6
# Напишите функцию, которая проверяет является ли число простым.
# Число передаётся в качестве параметра.
# Если число простое нужно вернуть из метода true, иначе false.

def prostoe_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
print(prostoe_number(9))

# Задание 7
# Напишите функцию, которая проверяет является ли шестизначное число «счастливым».
# Число передаётся в качестве параметра.
# Если число счастливое нужно вернуть из функции true, иначе false.
# «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна
# сумме трёх вторых цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
# а 723422 – несчастливое 7+2+3 != 4+2+2.

def is_lucky(num):
    """Проверка на счастливое число"""
    num1 = num // 100000
    num2 = (num // 10000) % 10
    num3 = (num // 1000) % 10
    num4 = (num // 100) % 10
    num5 = (num // 10) % 10
    num6 = (num // 1) % 10

    return num1 + num2 + num3 == num4 + num5 + num6

print(is_lucky(123321))
