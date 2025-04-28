def main():
    n = int(input())
    s = 0  
    # Обрабатываем каждый набор
    for _ in range(n):
        a, b, c = map(int, input().split())
        
        if a == 0:
            if b == c:
                s += 1  
        else:
            if (c - b) % a == 0 and (c - b) // a >= 0:
                s += 1
    print(s)
main()
