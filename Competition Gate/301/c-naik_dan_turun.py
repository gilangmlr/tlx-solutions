if __name__ == "__main__":
  n, q = [int(i) for i in input().split()]

  series = [0] * n

  for _ in range(q):
    t, x, y = [int(i) for i in input().split()]
    if t == 1:
      list1 = series[:x]
      list2 = [y] * x
      series[:x] = [a + b for a, b in zip(list1, list2)]
    elif t == 2:
      list1 = series[-x:]
      list2 = [y] * x
      series[-x:] = [a - b for a, b in zip(list1, list2)]

  series = [abs(i) for i in series]
  print(str(max(series)))