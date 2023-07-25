
# Задание 1
# Напишите программу, которая запрашивает два целых числа x и y,
# после чего вычисляет и выводит значение x в степени y.
x = int(input('введите целое число:'))
y = int(input('введите целое число:'))
print(x**y)
# или
x = int(input('введите целое число:'))
y = int(input('введите целое число:'))

for exp in range(1):
     print('число', x,'в степени', y, "равно",pow(x, y))

# Задание 2
# Подсчитать количество целых чисел в диапазоне от 100 до 999
# у которых есть две одинаковые цифры.

count = 0
for y in range(100,999,+1):
    a, b, c = str(y)
    if a == b or a == c or b == c:
        resultat = str(a) + str(b) + str(c)
        count += 1
print(count)

# Задание 3
# Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные.

count = 0
for y in range(1000,9999+1):
    a, b, c, d = str(y)
    if a != b and a != c and a != d and b != c and b != d and c != d:
        resultat = str(a) + str(b) + str(c) + str(d)
        count += 1
print(count)
count1 = 0
for y in range(100,999,+1):
    a, b, c = str(y)
    if a != b and a != c and b != c:
        resultat = str(a) + str(b) + str(c)
        count1 += 1
print(count1)
print("общий результат", count + count1) 

# count = 0  # счетчик чисел с разными цифрами
# for num in range(100, 10000):
#     # получаем каждую цифру числа
#     print (num)
#     first_digit = num // 1000
#     print (first_digit)
#     second_digit = (num // 100) % 10
#     print (second_digit)
#     third_digit = (num // 10) % 10
#     print (third_digit)
#     fourth_digit = num % 10
#     print (fourth_digit)
# # проверяем, что все цифры разные
#     if (num >= 1000 and first_digit != second_digit and first_digit != third_digit and first_digit != fourth_digit and second_digit != third_digit and second_digit != fourth_digit and third_digit != fourth_digit) or ( num <=1000 and second_digit !=third_digit and third_digit != fourth_digit and second_digit!=fourth_digit) :
#          count += 1
# print('Счетчик', count)

# Задание 4
# Пользователь вводит любое целое число.
# Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.
a = input("введите число:")
b = ''
for x in a:
    if x != "3" and x != "6":
        b += x
print(b)













