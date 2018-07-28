class SearchAndSort:
  @staticmethod
  def counting_sort(data):
    freq = {}
    for i in range(1, 100 + 1):
      freq[i] = 0
    for key in data:
      freq[key] += 1

    sorted_data = []
    for key, val in freq.items():
      if val > 0:
        for _ in range(val):
          sorted_data.append(key)
    return sorted_data

if __name__ == '__main__':
  n = int(input())

  data = []
  for _ in range(n):
    data.append(int(input()))
  data = SearchAndSort.counting_sort(data)
  med = 0
  if n % 2 == 0:
    mid = n // 2
    med = (data[mid - 1] + data[mid]) / 2
  else:
    med = data[n // 2]
  print('{0:.1f}'.format(med))

  
