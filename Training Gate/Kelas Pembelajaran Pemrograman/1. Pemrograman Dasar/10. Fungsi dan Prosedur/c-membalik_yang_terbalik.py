import sys

def reverse_decimal(x):
    temp = x
    ret = 0
    
    while temp > 0:
        ret = (ret * 10) + (temp % 10)
        temp //= 10

    return ret

a, b = sys.stdin.readline().split()
c = reverse_decimal(reverse_decimal(int(a)) + reverse_decimal(int(b)))

print(c)