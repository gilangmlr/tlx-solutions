import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()
s4 = sys.stdin.readline().rstrip()

s = s1.replace(s2, '')
s = s.replace(s3, s3 + s4)

print(s)