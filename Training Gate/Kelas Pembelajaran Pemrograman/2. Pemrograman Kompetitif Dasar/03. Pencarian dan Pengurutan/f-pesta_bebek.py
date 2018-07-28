class SearchAndSort:
  @staticmethod
  def insertion_sort_insert(data, el):
    data.append(el)
    sz = len(data)
    for i in reversed(range(1, sz)):
      if data[i] < data[i - 1]:
        temp = data[i]
        data[i] = data[i - 1]
        data[i - 1] = temp
      else:
        return i + 1
    return 1

if __name__ == '__main__':
  n = int(input())

  names = []
  for _ in range(n):
    name = str(input())
    print(SearchAndSort.insertion_sort_insert(names, name))
  
