import sys

word = list(sys.stdin.readline().rstrip())
rotation = int(sys.stdin.readline())

for i, char in enumerate(word):
    counter = 0
    while counter < rotation:
        char = chr(ord(char) + 1)
        if ord(char) > ord('z'):
            char = 'a'
        counter += 1
    word[i] = char
    
print(''.join(word))
