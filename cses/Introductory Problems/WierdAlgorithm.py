import sys

list = []
n = int(input())
while (n > 1):
    list.append(n)
    if n % 2 == 0: 
        n = n // 2
    else:
        n = n * 3 + 1
print(*list)