if __name__ == "__main__":
  scores = input().split()
  scores = [int(i) for i in scores]
  
  babak = sum(scores) // 7
  absolute_score = 4 * babak
  found = False
  for score in scores:
    if score == absolute_score:
      found = True
      break

  if found:
    print('YA')
  else:
    print('TIDAK')