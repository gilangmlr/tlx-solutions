import sys

n = int(sys.stdin.readline())

def dec_to_biner(n):
    if n == 1:
        return '1'
    if n == 0:
        return '0'
    
    if n % 2 == 1:
        return dec_to_biner(n // 2) + '1'
    else:
        return dec_to_biner(n // 2) + '0'

print(dec_to_biner(n))