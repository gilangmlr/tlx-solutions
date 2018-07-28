if __name__ == '__main__':
  n = 4
  start = 0
  stop = 1_000_000_000 + 1
  step = stop // n
  weights = [i for i in range(start, stop, step)]
  weights[0] = 1
  print(weights)