def two_sets(n):
    set1 = []
    set2 = []

    sum_of_numbers = n * (n + 1) / 2
    if sum_of_numbers % 2 != 0:
        return set1, set2

    numbers = []
    if n % 2 == 0:
        numbers = list(range(1, n + 1, 1))
    else:
        numbers = list(range(0, n + 1, 1))

    for idx in range(0, len(numbers) // 2):
        if idx % 2 == 1:
            set2.append(numbers[idx])
            set2.append(numbers[len(numbers) - 1 - idx])
        else: 
            if numbers[idx] != 0:
                set1.append(numbers[idx])
            set1.append(numbers[len(numbers) - 1 - idx])

    return set1, set2

set1, set2 = two_sets(int(input()))
if set1 and set2:
    print("YES")
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
else:
    print("NO")