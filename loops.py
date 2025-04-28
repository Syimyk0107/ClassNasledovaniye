#####  for  #####

# san = int(input('Enter your number: '))
# for i in range(san):
#     print('*' *10)

# sib = int(input('Enter your number: '))
# for i in range(1, 11):
#     print(f'{i}. {sib}')

# sib = int(input('Enter your number: '))
# for i in range(sib, 0, -1):
#     print('*' *i)


# num1 = int(input('Enter your first number: '))
# num2 = int(input('Enter your second number: '))
# for i in range(num1, num2, -2):
#     print(i)

# ###Таблица умножения
# number = int(input('Enter number N: '))
# print(f'Your number is {number}, and your solution is: ')
# for i in range(1, 11):
#     a = f' {number} X {i} = {number*i}'
#     print(a)

# ####строканы столбец кылып чыгаруу
# list = ['apple','lemon','banana']
# for i in list:
#     print(i)

# list = ['apple','phone','lemon','banana']
# for i in list:
#     if i == 'phone':
#         continue
#     print(i)


##### while #####

# i =1 
# while i < 101:
#     i+=1
#     if i == 51:
#         break
#     print(i)

# i =1 
# while i < 101:
#     i+=1
#     if i == 51:
#         continue
#     print(i)

##### Бесконечный цикл 1
# i=1
# while i != 0:
#     i+=1
#     print('Kyrgyzstan')

##### Бесконечный цикл 2
# while True:
#     print('Kyrgyzstan')  

##### ------------------------------------Homework  -------- ###########

# import random
# ques = input('Хотите ли вы играть в игры?(Да/Нет): ')
# if ques == 'Нет':
#     print('Отлично! Тогда учись!')
# elif ques == 'Да':
#     print('Отлично! Какую игру хочешь играть?')
#     print('1. "Угадай число"')
#     print('2. "Камень, ножницы и бумага"')
#     print('3. "Давай не будем играть"')
#     ch = input('Выберите номер игры(1-3): ')

#     if ch == '1':
#         print('Вы выбрали игру "Угадай число"')
#         number = random.randint(1,100)
#         s = 0
#         print('Выберите число от 1 дo 100')
#         while True:
#             num = int(input('Ваш выбор: '))
#             s+=1
#             if num < number:
#                 print('Выберите число по большее.')
#             elif num > number:
#                 print('Выберите число по меньшее') 
#             else:
#                 print('Поздраляю от души! Ты нашел что искал')
#                 break   

#     elif ch == '2':
#         print('Вы выбрали игру "Камень, ножницы и бумага"')
#         while True:    
#             list = ['камень', 'ножница','бумага']
#             comp_vibor = random.choice(list)
#             print('Выберите один из вариантов: камень, ножница или бумага')
#             vash_vibor = input()
#             if vash_vibor == comp_vibor:
#                 print(f'Ничья! Оба выбрали {vash_vibor}.')
#             elif(vash_vibor == 'ножница' and comp_vibor == 'камень') or \
#                 (vash_vibor == 'бумага' and comp_vibor == 'ножница') or \
#                 (vash_vibor == 'камень' and comp_vibor == 'бумага'):
#                 print(f'Ты проиграл! Ваш противник выбрал {comp_vibor}.')
#             else:        
#                 print(f'Ты выиграл, повезло! Ваш противник выбрал  {comp_vibor}.')
#                 break
#     elif ch == '3':
#         print('Вы выбрали игру "Давай не будем играть"')
#         print('Отличный выбор, родной! Пора спать!')


