def is_odd_in_decimal(number):
    # Проверяем, сколько нечетных цифр в числе
    odd_digits = {'1', '3', '5', '7', '9'}
    count_odd_digits = sum(1 for digit in str(number) if digit in odd_digits)
    
    # Число четное, если количество нечетных цифр чётное
    return count_odd_digits % 2 != 0

def is_odd_in_binary(number):
    # Переводим число в двоичную систему
    binary_representation = bin(number)[2:]  # Преобразуем число в строку без '0b' префикса
    # Считаем количество единичных битов
    ones_count = binary_representation.count('1')
    
    # Число нечетное, если количество единичных битов нечётное
    return ones_count % 2 != 0

def determine_parity(number):
    # Проверяем на четность по обеим системам
    if is_odd_in_decimal(number) and is_odd_in_binary(number):
        return "ODD"
    else:
        return "EVEN"

# Пример использования
number = int(input())
print(determine_parity(number))
