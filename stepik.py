# a = 7
# b = -4
# c = 3
# print(a,b,c,sep='\n') #вывод в столбик в принте

# s1 = "Hello"
# s2 = "Balakirev"
# print("Hello",end=" ")
# print("Balakirev")  #Hello Balakirev

# s1, s2 = map(str.strip, input().split())
# print('Word 1:',s1,'|'  ' Word 2:', s2)

# a,b = map(int, input().split())
#
# print(a**b)

# a, b = map(float, input().split())
# print(a + b)

# X, Y = map(int, input().split())
# black = X * 2
# green = Y * 4
# print(X + Y + black + green)

# shirina = int(input(''))
# dlina = int(input(''))
# print(shirina + dlina *2)

# import math
# print(round(math.pi,3))

# Подвиг 12. Составить программу вывода на экран вещественного числа, вводимого с клавиатуры.
# Выводимому числу должно предшествовать сообщение "Вы ввели число" (без кавычек).
# a = float(input(''))
# print('Вы ввели число',a )

# Вводится вещественное число. Нужно определить, что его целая часть кратна 3.
# На экран вывести True,
# если кратно и False - в противном случае.
# Задача делается без использования условного оператора.
# a= float(input())
# a = int(a)
# print(a % 3 == 0)

# Подвиг 6. Вводится стоимость книги X рублей (например, X = 435.78) - положительное вещественное число с точностью до сотых
# (два знака после запятой). Требуется определить, является ли дробное значение (число после запятой) больше 50.
# На экран вывести True, если больше и False - в противном случае.
# price = 435.78#float(input())
# print((price % 1 )>0.50)

# Подвиг 7. Вводятся два целочисленных значения в одну строчку через пробел. Можно прочитать с помощью команды:
#
# a, b = map(int, input().split())
#
# Необходимо определить, можно ли первое число нацело разделить на второе.
# На экран вывести True, если делится и False - в противном случае.
# a, b = map(int, input().split())
# print(a % b == 0)

# Подвиг 10. Вводятся три целых положительных числа. Прочитать в переменные их можно с помощью команды:
#
# a, b, c = map(int, input().split())
#
# Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника.
# Напомню, что сумма длин двух произвольных сторон всегда должна быть больше третьей стороны. На экран вывести True,
# если треугольник формируется и False - в противном случае.

# a, b, c = map(int, input().split())
# print(a + b > c and a + c >b and b + c > a)

# Подвиг 11. Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон [0; 2] или в диапазон [10; 20]
# (включительно). На экран вывести True, если попадает и False - в противном случае.

# numbers = float(input())
# print(numbers>=0 and numbers<=2 or numbers>=10 and numbers<=20)

# Подвиг 7. Напишите программу ввода двух слов через пробел.
# Сформируйте новую строку, продублировав первое слово дважды, а второе - трижды
# (все слова в результирующей строке должны идти через пробел).Результат выведите на экран.
# a, b = input().split()
# print(((a+' ')*2) + ((b+' ')*3))


