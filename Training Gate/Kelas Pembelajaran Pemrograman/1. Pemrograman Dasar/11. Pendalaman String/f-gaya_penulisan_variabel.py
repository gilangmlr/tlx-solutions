import sys
import re

s = str(sys.stdin.readline()).rstrip()

ss = ''
if '_' in s:
    ss = re.sub('_(.)', lambda m: m.group(1).upper(), s)
else:
    ss = re.sub('([A-Z])', lambda m: '_' + m.group(1).lower(), s)

print(ss)