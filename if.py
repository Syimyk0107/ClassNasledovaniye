####-----if------#### 
####-----elif----####
####-----else----####

# a = 5
# b = 5
# if a > b:
#     print('a big than b')
# elif a < b:
#     print('b big than a')
# else:  
#     print('b equal to a')

# days = int(input('Enter number: '))
# if days == 1:
#     print('Monday')
# elif days == 2:
#     print('Tuesday')   
# elif days == 3:
#     print('Wednesday')    
# elif days == 4:
#     print('Thusday')
# elif days == 5:
#     print('Friday')   
# elif days == 6:
#     print('Saturday')
# elif days == 7:
#     print('Sunday')   
# else:
#     print('this is not a day at the weekend')     


# point = int(input('Enter your point: '))
# if 50 <= point < 60:
#     print('your grade is 3')
# elif 60 <= point < 80:
#     print('your grade is 4') 
# elif 80 <= point <= 100:
#     print('your grade is 5')
# else:
#     print('non-admission') 

###Calculator

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: ')) 
# c = input('enter your operator: ') 
# if c == '*':
#     print('Your solution: ',a * b)
# elif c == '/':
#     print('Your solution: ',a / b)
# elif c == '+':  
#     print('Your solution: ',a + b)
# else:  
#     print('Your solution: ',a - b)

####Head or Tail
# import time  ###modul or paket 
# import random  ###Модуль же пакет

# num = random.randint(1, 2)
# print('This is a game "Head or Tail"')
# if num == 1:
#     time.sleep(2) ##задержка времени
#     print('Head')
# elif num == 2:
#     time.sleep(2)
#     print('Tail')


# # my_list = ['Syimyk','12345']
# base1 = 'Syimyk'
# base2 = '12345'
# login = input('enter your login: ')
# passport = input('enter your passport: ') 
# if login == base1 and passport == base2:
#     print('Your login and passport correct. Welcome to site!')
# else:
#     print('non-correct login or passport')


###### Pay with credit card
# import time  ###modul or paket 
# base1 = 'Syimyk'
# base2 = '12345'
# num = 5000
# login = input('enter your login: ')
# password = input('enter your passport: ') 
# n = int(input('Enter your number: '))

# if login == base1 and password == base2 and num <= n:
#     print('Your login and password correct!')
#     print('Debiting from the account. Please waiting...')
#     time.sleep(5) ##задержка времени
#     print('Payment complated successfully!!!')

# elif login == base1 and password == base2 and num > n:
#     print('Your login and password correct!')
#     print('Debiting from the account. Please waiting...')
#     time.sleep(5) ##задержка времени
#     print('Payment failed. Infsufficient funds on the card.')
 
# elif login != base1 or password != base2:
#     print('non-correct login or password')
#     time.sleep(2) ##задержка времени
#     print('Payment failed.')


# import time  ###modul or paket 
# import random  ###Модуль же пакет
# num = random.randint(1, 100)
# print('Привет! Давай поиграем в "угадай число"')
# print('Я загадал число от 1 до 100. Попробуй угадать!')
# n = int(input('Твоё предположение: '))

# if num < n :
#     time.sleep(3) ##задержка времени
#     print('Введите число меньшее')
    
# elif num > n:
#     time.sleep(3) ##задержка времени
#     print('Введите число большее')
    
# else:
#     time.sleep(3) ##задержка времени
#     print('Поздравляю! Вы угадали числу')


# date = input('Enter your month: ')
# if date == 'Январь':
#     print('Водолей')
# elif date == 'Февраль':
#     print('Рыбы')
# elif date == 'Март':
#     print('Овен')
# elif date == 'Апрель':
#     print('Телец') 
# elif date == 'Май':
#     print('Близнецы')
# elif date == 'Июнь':
#     print('Рак')
# elif date == 'Июль':
#     print('Лев')
# elif date == 'Август':
#     print('Дева')   
# elif date == 'Сентябрь':
#     print('Весы')
# elif date == 'Октябрь':
#     print('Стрелец')
# elif date == 'Ноябрь':
#     print('Скорпион')
# elif date == 'Декабрь':
#     print('Козерог') 

