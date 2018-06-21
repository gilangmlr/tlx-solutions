import sys

s, t = sys.stdin.readline().split()

while t in s:
    s = s.replace(t, '')

print(s)