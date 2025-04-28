# ##Множества (set)
# ##Неупорядоченные коллекции уникальных элементов
# ##Примеры
# my_set = {1, 2, 'apple', 3.14}

# ## add():Добавляет элемент в множество
# my_set = {1, 2, 3}
# my_set.add(4)   #my_set = {1, 2, 3, 4}

# ##remove()  Удаляет элемент из множества; если элемента нет, вызывает ошибку
# numbers = {1, 2, 3, 4}
# numbers.remove(3) #numbers = {1, 2, 4}

# ##union() Объединение двух множеств
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2) #uninon_set = {1, 2, 3, 4, 5}

# ##intersection() Пересечение двух множеств
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# intersection_set = a.intersection(b) #intersection_set={3, 4}

# ##pop() Удаляет и возвращает случайный элемент из множества
# colors = {'red','green','blue'}
# removed_colors = colors.pop()  #removed_colors is a random element

# ##discard()  Удаляет элемент из множества, если он присутствует
# my_set = {1,2,3}
# my_set.discard(2)  #my_set = {1,2}

# ##Получение подкортежа с определенным диапазоном индексов
# my_tuple = (10, 20, 30, 40, 50)
# subtuple = my_tuple[1:4]  #subtuple=(20,30,40)

# ## Шаг срезка для кортежа
# items = ('apple','orange','banana','grape')
# sliced_items = items[::2] #sliced_items=('apple','banana')

# №1111
# a = {1,2,3,4,5}
# a.remove(3) 
# print(a)

# ####22222
# strok = {'red','green','blue'}
# strok.add('yellow')
# print(strok)

# ##333333
# numbers = [22, 44, 51, 14, 30]
# ob_numbers = numbers[0:3]
# print(ob_numbers)
# my_tuple = (10, 20, 30, 40, 50)
# subtuple = my_tuple[0:3] 
# print(subtuple)
# #4444
# a = {1, 2, 3, 4}
# b = {35, 44, 12, 25}
# union_mn = a.union(b)
# print(union_mn)

# ##55555
# ##1variant
# txt = "Hello World, I see you"
# txt = txt.replace("World", "Bishkek")
# print(txt)
# # mylist = ['apple', 'banana', 'cherry']
# # mylist.pop(1)
# # print(mylist)
# #2 variant
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)