class SearchAndSort:
  @staticmethod
  def bubble_sort(data):
    sz = len(data)
    for i in range(sz):
      swapped = False
      for j in range(sz - 1, i, -1):
        if len(data[j]) < len(data[j - 1]) or (len(data[j]) == len(data[j - 1]) and data[j] < data[j - 1]):
          swapped = True
          temp = data[j]
          data[j] = data[j - 1]
          data[j - 1] = temp
      if not swapped:
        break

if __name__ == '__main__':
  n = int(input())

  names = []
  for _ in range(n):
    names.append(str(input()))
  
  SearchAndSort.bubble_sort(names)
  print('\n'.join(names))
  
