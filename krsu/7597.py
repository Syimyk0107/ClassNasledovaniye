from collections import Counter
n = int(input())
letters = input()

count = Counter(letters)

ako_count = min(count.get('a', 0), count.get('k', 0), count.get('o', 0))

erilin_count = min(
    count.get('e', 0),
    count.get('r', 0),
    count.get('i', 0) // 2,
    count.get('l', 0),
    count.get('n', 0)
)

print(f"{ako_count} {erilin_count}")
