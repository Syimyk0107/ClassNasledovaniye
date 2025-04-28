try:
    x = 1 / 0
except ZeroDivisionError:
    print("Нельзя делить на ноль")
# Программа:
try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Ошибка: деление на ноль")