def missing_number(n, nums):
    req_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return req_sum - actual_sum

n = int(input())
nums = [int(i) for i in input().split()]
print(missing_number(n, nums))