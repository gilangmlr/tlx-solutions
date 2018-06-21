import sys

s = list(sys.stdin.readline())
s.pop()
k = int(sys.stdin.readline())

chs = [ord(i) + k for i in s]
chs = [chr(i) if i <= ord('z') else chr((i % ord('z')) + (ord('a') - 1))  for i in chs]

print(''.join(chs))