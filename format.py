# name = input('Enter your login: ')
# age = int(input('Great your parol: '))
# a = f'Your login {name}, and parol {age} saved !'
# print(a)

# name = input('Enter your name: ')
# a = len(name)
# a = f'Your name is {name}, and in your name have {a} letters !'
# print(a)


number = int(input('Enter your number: '))
print(f'Your number is {number}, and your solution is: ')
[print(f' {number} X {i} = {number*i}')for i in range(1,11)]