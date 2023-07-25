# numbers=[10, 5, 7, 2, 1, 8]
# print('до удаления', len(numbers))
# del numbers[5]
# print(len(numbers))
# print('после удаления', len(numbers))
# print(numbers[5])

# numbers=[10, 5, 7, 2, 1, 8]
# print('до удаления', len(numbers))
# del numbers[5] # при удалении или вызове элемента с - отcчет идет с 1,а не с 0
# print(len(numbers))
# print('после удаления', len(numbers))
# print(numbers[-5])

# numbers=[10, 5, 7, 2, 1, 8]
# numbers.append(15) #прибавляет значение в конец списка
# print(len(numbers)) # прибавляет количество к длинне списка
# print(numbers)

# list = []
# for i in range(17):
#     list.append(i)
#     print(list)

# x=int(input())
# y=int(input())
# list=[]
# for i in range(x, y):
#     list.append(i)
# print(i) # показывает что внутри диапазона

# x=4#int(input())
# y=7#int(input())
# list=[]
# for i in range(x, y):
#     list.append(i)
# print(list) # показывает список без последнего значения


# x=4#int(input())
# y=10#int(input())
# list=[]
# for i in range(x, y):
#     list.insert(3,i) # ставится 1 локация, 2значение
# print(list)


# list=[]
# for i in range(5):
#     list.insert(0,i+1) # обратный порядок
# print(list)

# mylist=[1,2,3] # сложение
# total = 0
# for i in range(len(mylist)):
#     total+=i
#     print(total)
# print(total)

# mylist=[10,1,8,3,5]
# length = len(mylist) #length=5
# print(length)
# for i in range(length//2):
#     mylist[i], mylist[length-i-1], mylist[length-i-1], mylist[i]
#     print(i)
# print(mylist)

# сортировка пузырьком
# myList = [8, 10, 6, 2, 4]  # список для сортировки
# for i in range(len(myList) - 1):
#     # нам нужно (5 — 1) сравнений
#     if myList[i] > myList[i + 1]:
#         # сравниваем соседние элементы
#         myList[i], myList[i + 1] = myList[i + 1], myList[i]
# # если мы окажемся здесь, это означает,
# # что мы должны поменять местами элементы
# print(myList)
#
# myList = [8, 10, 6, 2, 4] # список для сортировки
# swapped = True # небольшое жульничество –
# while swapped: # нам необходимо ввести цикл while
#  swapped = False # никакого обмена местами
#  for i in range(len(myList) - 1):
#      if myList[i] > myList[i + 1]:
#          swapped = True # произошёл обмен местами!
#          myList[i], myList[i + 1] = myList[i + 1],myList[i]
# print(myList)

# myList = [8, 10, 6, 2, 4]
# myList.sort() # сортировка
# print(myList)
# [2, 4, 6, 8, 10]
#
# myList = [8, 10, 6, 2, 4]
# myList.reverse() # обратный порядок
# print(myList)

# list1 = [1]
# list2 = list1# приравнивая один список к другому будет одно и тоже значение
# list1[0] = 2
# print(list2)
#
# list1 = [1]
# list2 = list1[:]#  срез [:]
# list1[0] = 2
# print(list2)



# list1 = [8, 10, 6, 2, 4]
# list2 = list1[1:4]#  срез [:] срез делается по индексам
# list1[0] = 2
# print(list2)

# list1 = [8, 10, 6, 2, 4]
# list2 = list1[1:-1]#  срез [:] срез делается по индексам
# list1[0] = 2
# print(list2)

# list1 = [8, 10, 6, 2, 4]
# list2 = list1[0:]#  срез [:]
# print(list2)

# myList = [10, 8, 6, 4, 2]
# newList = myList[:1]
# print(newList)

#строки


# a='мама мыла раму'
# print(len(a)) # считает длину строки

# str1 = 'a'
# str2 = 'b'
# print(str1+str2)#сложение строк
# print(5*str2) #умножение строк

# str1 = 'a'
# str2 = 'b'
# print(ord(str1)) # узнать номер кодовой точки ord

# str1 = 'abcdejku'
# print(min(str1)) # узнать самую легкую букву
#
# str1 = 'abcd ejku'
# print(str1.index('c')) # узнать индекс буквы

# str1 = 'abcd ejku'
# print(list(str1)) # переводит каждую букву в строку

# str1 = 'abcd ejku'
# print(str1.count('4'))#

# str1 = 'abJHGFDDSd ejku'
# print(str1.capitalize())# меняет первую букву в верхни регистр а остальные в нижний
#
# str1 = 'abJHGFDDSd ejku'
# print(str1.capitalize())

# str1 = 'abJHGFDDSd ejku'
# print(','.join(['помидоры','яблоки'])) # записывает строку

# print("www.cisco.com".lstrip('w.')) # удаляет только с начала

print("мама мыла раму".replace("мыла","протирала", 1)) # заменяет слово на слово последний индекс слова

print("www cisco com".title()) # каждое слово и меняет первую букву на верхний регистр