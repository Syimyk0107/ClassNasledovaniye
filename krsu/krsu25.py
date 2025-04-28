from collections import Counter

def main():
    N = int(input())  
    queries = [input().strip() for _ in range(N)]  # Считываем все запросы

    # Подсчитываем частоту запросов
    count = Counter(queries)
    
    # Сортируем запросы: по частоте (по убыванию), затем по алфавиту (по возрастанию)
    sorted_queries = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    # Выводим только первые 10 запросов (если их меньше, выводим все)
    for i in range(min(10, len(sorted_queries))):
        print(sorted_queries[i][0])


main()
