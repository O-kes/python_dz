# Задание 1
# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел.
# Результат вычислений вывести на экран.
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
summa = num1 + num2 + num3
proizvedenie = num1 * num2 * num3
print("Сумма введенных чисел: ", summa, "Произведение введенных чисел: ",proizvedenie)


# Задание 2
# Пользователь вводит с клавиатуры три числа.
# Первое число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке,
# третье число — задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат.

num1 = int(input("Введите вашу ежемесячную зарплату: "))
num2 = int(input("Введите вашу сумму ежемесячного платежа по кредиту: "))
num3 = int(input("Введите вашу задолжность по коммунальным услугам: "))
rashod = num1 - num2 - num3
print("Остаток за вычетом всех расходов", rashod)

# Задание 3
# Напишите программу, вычисляющую площадь ромба.
# Пользователь с клавиатуры вводит длину двух его диагоналей.

d1 = int(input("Введите первую диагональ: "))
d2 = int(input("Введите вторую диагональ: "))
formula = 1 / 2 * d1 * d2
print("Площадь ромба", formula)

# 4 Выведите на экран надпись To be or not to be на разных строках. Пример вывода:
# To be
# or not
# to be
print("To be")
print("or not")
print("to be")
'''или'''
print("To be \nor not \nto be")

# 5 Выведите на экран надпись «Life is what happens when you're busy making other plans»
# John Lennon на разных строках. Пример вывода:
# “Life is what happens
#      when
#         you’re busy making other plans”
#                                     John Lennon.
print("Life is what happens ")
print("     when")
print("        you're busy making other plans")
print("                                    John Lennon.")
