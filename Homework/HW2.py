'''
1.	Дана строка состоящая минимум из 6 символов.
- Сначала выведите третий символ этой строки.
- Во второй строке выведите предпоследний символ этой строки.
- В третьей строке выведите первые пять символов этой строки.
- В четвертой строке выведите всю строку, кроме последних двух символов.
- В пятой строке выведите все символы с четными индексами
- В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
- В седьмой строке выведите все символы в обратном порядке.
- В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
- В девятой строке выведите длину данной строки.
'''

# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[:-2:2])
# print(s[1:-2:2])
# print(s[::-1])
# print(s[::-2])
# len(s)

'''
2.	Дано слово. Верно ли, что оно начинается и оканчивается на одну и ту же букву?'''

# s[0] == s[-1]

'''
3.	Дано слово. Получить его часть, образованную второй, третьей и четвертой буквами.'''

# print(s[1:5])

'''
4.	Из слова яблоко путем "вырезок" и "склеек" его букв получить слова блок и око.'''

# s = 'яблоко'
# print(s[1:-1])
# print(s[-3:])

'''
5.	В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"'''

# s = 'Ivanou Ivan'
# print(s[-4:] + ' ' + s[:-5])

'''
6.	Проверить является ли строка палиндромом.(шалаш).'''

# list1 = list('шалаш')
# print(list1 == list1[::-1])

'''
7.	Создайте список и извлеките из него списка второй элемент.'''

# list1 = list('шалаш')
# print(list1[1])


'''
8.	Вывести входит ли строка1 в строку2 (пример: employ и employment )'''

# s1 = 'employ'
# s2 = 'employment'
# print(s1 in s2)


'''
9.	*Дана строка которая содержит более 2 символов ‘f’. Строка может быть произвольной.
 Найдите индекс второй буквы ‘f’ в данной строке. '''

s = ("qweqwefwqeqwef")
print(s.index('f'), s.index('f',s.index('f')+1))



'''
10.	*Создайте словарь, связав его с переменной school, и наполните его
данными которые бы отражали количество учащихся в десяти разных
классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).Внесите изменения в словарь согласно следующему: 
а) в одном из классов изменилось количество учащихся
б) в школе появился новый класс.
в) в школе был расформирован (удален) другой класс. 
г) Вычислите общее количество учащихся 9 классов в школе.

'''
