import sys

s = sys.stdin.readline().rstrip()

def pal(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s.endswith(s[0]):
        return pal(s[1:-1])
    return False

print("YA" if pal(s) else "BUKAN")