class SearchAndSort:
  @staticmethod
  def bubble_sort(data):
    sz = len(data)
    for i in range(sz):
      swapped = False
      for j in range(sz - 1, i, -1):
        if data[j][0] > data[j - 1][0]:
          swapped = True
          temp = data[j]
          data[j] = data[j - 1]
          data[j - 1] = temp
      if not swapped:
        break

if __name__ == '__main__':
  n, k = [int(el) for el in input().split()]

  w = [int(el) for el in input().split()]
  c = [int(el) for el in input().split()]
  cw = []
  for key, val in enumerate(w):
    tupple = (c[key]/val, val)
    cw.append(tupple)
  SearchAndSort.bubble_sort(cw)
  
  wc = 0
  p = 0
  for price, weight in cw:
    for _ in range(weight):
      wc += 1
      p += price
      if wc == k:
        break
    if wc == k:
      break

  print('{0:.5f}'.format(p))
  
