# метод count()
print('Oльгаааа'.count('а')) #подсчитывает количество
                            #буквы должны соответствовать языку и регистру,
# метод index()
# str1 = 'abcd ejku'
# print(str1.index('c')) # узнать индекс буквы

# Метод capitalize()
# str1 = 'abJHGFDDSd ejku'
# print(str1.capitalize())# меняет первую букву в верхни регистр а остальные в нижний

# Метод center()
# print('['+ 'Ольга'.center(10) +']') #отсортирует слово по центру 10
# print('[' + 'gamma'.center(20, '*') + ']') #center() с двумя параметрами использует
                                          # символ из второго аргумента вместо пробела
# Метод endswith()
# if 'Oльга'.endswith('га'):#endswith() проверяет, заканчивается ли данная строка указанным аргументом,
#                           # и возвращает True или False
#     print('да')
# else:
#     print('нет')

#Метод find()        #он ищет подстроку и возвращает индекс первого появления этой подстроки
# print('Oльга'.find('га'))
# t = 'theta'             #find(), если вы толь- ко хотите проверить,
                          #встречается ли отдельный символ в строке
# print(t.find('eta'))
# print(t.find('et'))
# print(t.find('the'))
# print(t.find('ha'))

# print('kappa'.find('a', 2))      #find() с двумя параметрами

# Метод isalnum()
# print('Oльга'.isalnum()) #isalnum() проверяет,
                       # содержит ли строка только цифры или символы алфавита (буквы),
                       # и возвращает True или False в соответствии с результатом.
# t = 'Six lambdas'      #пробел не цифра не буква
# print(t.isalnum())
# t = 'ΑβΓδ'
# print(t.isalnum())
# t = '20E1'
# print(t.isalnum())

# Метод isalpha() #isalpha() только буквы
# print('Oльга'.isalpha())

# Метод isdigit()
# print('0123'.isdigit()) #isdigit() только цифры

# Метод islower()
# print('бббббтит'.islower()) # islower() подвариант isalpha()принимает только строчные буквы.

# Метод isupper()           #isupper() является версией islower() для верхнего регистра —
# print('ОЛЬГА'.isupper())    # он концентрируется только на заглавных буквах.

# Метод isspace()
# print(' '.isspace())  # isspace() идентифицирует только пробельные символы —
                        # он игнорирует любой другой символ (тогда результатом является False).

# Метод join()           Метод join() довольно сложен
                         # ■ как следует из его названия, метод выполняет соединение —
# str1 = 'abJHGFDDSd ejku'
# print(','.join(['помидоры','яблоки'])) # записывает строку

                        # он требует один аргумент в виде списка; необходимо убедиться,
                        # что все элементы списка являются строками
                        # — в противном случае метод сгенерирует исключение TypeError;
                        # ■ все элементы списка будут объединены в одну строку, но...
                        # ■ ...строка, из которой был вызван метод,
                        # используется в качестве разделителя, помещенного среди строк;
                        # ■ вновь созданная строка возвращается в качестве результата.

# Метод lower()          #lower() создает копию исходной строки, заменяет все буквы
                         # в верхнем регистре их аналогами в нижнем регистре
                         # и возвращает строку в качестве результата.
                         # Опять же, исходная строка остается нетронутой.
                         # Если строка не содержит символов верхнего регистра,
                         # метод возвращает исходную строку.
                         #Примечание: метод lower() не принимает никаких параметров.

# Метод lstrip()
# print("www.cisco.com".lstrip('w.')) # удаляет только с начала

# Метод replace()        #replace() с двумя параметрами возвращает копию исходной строки,
# print("мама мыла раму".replace("мыла", "протирала",1)) # заменяет слово на слово последний индекс слова
                         # в которой все вхождения первого аргумента были заменены
                         # вторым аргументом.

# Метод rfind()          #rfind() выполняют почти те же функции, что и их аналоги
# print('Oльга'.rfind('O'))# (лишенные префикса r), но начинают поиск с конца строки,
                         # а не с начала (следовательно, префикс r означает right).

# Метод rstrip()
# print("www.cisco.com".lstrip('.com'))   # удаляет с конца

# Метод split()                      #Метод split() разбивает строку и создает список всех
# print('O-л-ь-г-а'.split('-'))      # обнаруженных подстрок.
#выдача ['O', 'л', 'ь', 'г', 'а']    # Метод предполагает, что подстроки разделены пробелами
# print('Oльга Кес'.split(' '))        # — пробелы не участвуют в операции и не копируются
#выдача ['Oльга', 'Кес']             # в результирующий список.
                                     # Если строка пуста, результирующий список тоже пуст.

# Метод startswith()
# text = "Some not very long string"  #startswith() является зеркальным отражением endswith()
# text.startswith("S")                # — он проверяет, начинается ли заданная строка
# text.startswith("Some")
# print (text.startswith("S") )
# True
# print (text.startswith("Some"))        # с указанной подстроки.
# True

# Метод strip()                      #trip() объединяет действие методов rstrip() и lstrip()
# print('['+   '   Oльга '.strip()   +']')    # — создает новую строку,
# [Oльга]                                    # в которой отсутствуют все начальные и конечные пробелы

# Метод swapcase()   #swapcase() создает новую строку, меняя регистр всех букв в исходной строке:
# print('Oльга'.swapcase())                    # символы нижнего регистра становятся прописными, и наоборот.
# oЛЬГА

# Метод title()
# print("www cisco com".title()) # каждое слово меняет первую букву на верхний регистр

# Метод upper()                               #upper() создает копию исходной строки,
# print('Oльга'.upper())                        # заменяет все строчные буквы их
                                             # прописными аналогами и возвращает
                                             # строку в качестве результата.
