def is_palindrome(n):
    return str(n) == str(n)[::-1]

def count_palindromes(a, b):
    count = 0
    for number in range(a, b + 1):
        if is_palindrome(number):
            count += 1
    return count

A, B = map(int, input().split())

result = count_palindromes(A, B)
print(result)
