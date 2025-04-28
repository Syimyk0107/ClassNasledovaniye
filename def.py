# def main():
#     print('Hello')
#     a = 5
#     b = 3
#     print(a+b)
# main()

# def main():
#     print('Hello')
#     print('Wold')
#     print('Salam')

# main()
# print('-----')
# main()

# num = int(input('Enter your number: '))
# def table():
#     print(f'Tab umnoj for {num} ')
#     for i in range (1, 11):
#         result = i * num
#         print(f'{i} x {num} = {result}')
# table()        
##########---------------Calculator
# a = int(input('Enter your first number: '))
# b = int(input('Enter your second number: '))
# def calc():
#     opr = input('Choose your math operator: "+" "-" "*" or "/": ')
#     if opr == '+':
#         print(a+b)
#     elif opr == '-':
#         print(a-b)
#     elif opr == '*':
#         print(a*b) 
#     elif opr == '/' and b!=0:
#         print(a/b)   
#     elif opr == '/' and b==0:
#         print("You don't divide number to zero")

# calc()        

# a = int(input('Enter your first number: '))
# b = int(input('Enter your second number: '))
# def calc():
#     opr = input('Choose your math operator: "+" "-" "*" or "/": ')
#     if opr == '+':
#         print(a+b)
#     elif opr == '-':
#         print(a-b)
#     elif opr == '*':
#         print(a*b) 
#     elif opr == '/' and b!=0:
#         print(a/b)   
#     elif opr == '/' and b==0:
#         print("You don't divide number to zero")

# calc()        

# a = int(input('Enter your first number: '))
# b = int(input('Enter your second number: '))
# def calc():
#     opr = input('Choose your math operator: "+" "-" "*" or "/": ')
#     if opr == '+':
#         print(a+b)
#     elif opr == '-':
#         print(a-b)
#     elif opr == '*':
#         print(a*b) 
#     elif opr == '/' and b!=0:
#         print(a/b)   
#     elif opr == '/' and b==0:
#         print("You don't divide number to zero")

# calc()        

###-------------------------Game "Guess the word"##############################
# import random
# def find():
#     while True:
#         print('Let"s play the game "Guess the word": ')
#         wrd = input('Enter your word: ')
#         rndwrd = ["apple", "banana", "cherry","grape"]
#         random_ele = random.choice(rndwrd)  ###choice----тексттен рандомно тандоодо колдонобуз
#         if wrd == random_ele:
#             print("Congrat! You are find the word!:")
#             break        
#         else:
#             print('Choose different word')
# find()


####  ----------------------"Камень, ножницы и бумага"#######################
# import random
# def play():
#     print('Вы выбрали игру "Камень, ножницы и бумага"')
#     while True:    
#         list = ['камень', 'ножница','бумага']
#         comp_vibor = random.choice(list)
#         print('Выберите один из вариантов: камень, ножница или бумага')
#         vash_vibor = input()
#         if vash_vibor == comp_vibor:
#             print(f'Ничья! Оба выбрали {vash_vibor}.')
#         elif(vash_vibor == 'ножница' and comp_vibor == 'камень') or \
#             (vash_vibor == 'бумага' and comp_vibor == 'ножница') or \
#             (vash_vibor == 'камень' and comp_vibor == 'бумага'):
#             print(f'Ты проиграл! Ваш противник выбрал {comp_vibor}.')
#         else:        
#             print(f'Ты выиграл, повезло! Ваш противник выбрал  {comp_vibor}.')
#             break
# play()


def kvad(san):
    print(f'kvadrat {san} = {san*san}')
kvad(5)
kvad(6)
kvad(10)
