if __name__ == "__main__":
  s1 = str(input())
  s2 = str(input())

  is_possible = False
  for index, val in enumerate(s1):
    if s1[:index] + s1[index + 1:] == s2:
      print('Tentu saja bisa!')
      is_possible = True
      break

  if not is_possible:
    print('Wah, tidak bisa :(')