# def is_perfect_number(n):
#     sum_deliteley = sum(i for i in range(1, n) if n % i == 0)
#     if sum_deliteley == n:
#         return "Yes"
#     else:
#         return "No"
# n = int(input())
# print(is_perfect_number(n))

import math

def perfect_number(n):
    if n <= 1:
        return "No"
    
    sum_delitley = 1 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_delitley += i
            if i != n // i:
                sum_delitley += n // i
    
    if sum_delitley == n:
        return "Yes"
    else:
        return "No"

n = int(input())
print(perfect_number(n))
