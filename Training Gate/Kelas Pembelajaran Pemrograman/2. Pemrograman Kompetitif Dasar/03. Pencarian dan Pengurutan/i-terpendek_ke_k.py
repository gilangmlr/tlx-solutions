class SearchAndSort:
  @staticmethod
  def bubble_sort(data):
    sz = len(data)
    for i in range(sz):
      swapped = False
      for j in range(sz - 1, i, -1):
        if data[j] < data[j - 1]:
          swapped = True
          temp = data[j]
          data[j] = data[j - 1]
          data[j - 1] = temp
      if not swapped:
        break

if __name__ == '__main__':
  n, k = [int(el) for el in input().split()]

  heights = [int(el) for el in input().split()]
  SearchAndSort.bubble_sort(heights)
  
  print(heights[k - 1])
  
