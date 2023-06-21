largest_number = -99999999999999
number = int(input("Введите число или напишите -1, чтобы остановить программу: "))
while number != -1:
    if number > largest_number:
        largest_number = number
    print("Смена значения:", largest_number)
    number = int(input("Введите число или напишите -1,  чтобы  остановить программу: "))
    print("Наибольшее число:", largest_number)














