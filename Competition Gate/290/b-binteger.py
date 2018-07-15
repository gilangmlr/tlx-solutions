import sys

n = int(sys.stdin.readline())

nums = []

while n > 0:
    if n % 2 == 0:
        nums.append(0)
    else:
        nums.append(1)
    n //= 2

print(''.join([str(i) for i in reversed(nums)]))