class DuckWeight:
  def __init__(self, _ducks, _weight_queries):
    self.ducks = _ducks
    self.weight_queries = _weight_queries
  
  def find(self):
    for x, y in self.weight_queries:
      total = -1
      x_index = 0
      y_index = len(self.ducks) - 1
      if total < 0 and x == y or y < self.ducks[x_index] or x >= self.ducks[y_index]:
        total = 0
      if total < 0 and x < self.ducks[x_index] and y >= self.ducks[y_index]:
        total = len(self.ducks)

      x_index = self.binary_search(x, '>')
      
      y_index = self.binary_search(y, '<=')
      
      if total < 0 and x_index >= y_index:
        if x_index > y_index:
          total = 0
        elif self.ducks[x_index] > x and self.ducks[y_index] <= y:
          total = 1
        else:
          total = 0
      
      if total < 0:
        total = y_index - x_index + 1
      
      # print('{}, x_idx: {}, y_idx: {}, x: {}, y: {}'.format(total, x_index, y_index, x, y))
      print(str(total))
      
  def binary_search(self, weight, inequality):
    lower = 0
    upper = len(self.ducks) - 1

    middle = (upper + lower) // 2
    while lower <= upper:
      middle = (upper + lower) // 2
      weight_middle = self.ducks[middle]
      if weight_middle == weight:
        if '=' in inequality:
          return middle
        elif '<' in inequality:
          return middle - 1
        else:
          return middle + 1
      elif weight < weight_middle:
        upper = middle - 1
        if lower > upper and '<' in inequality:          
          middle = upper
      else:
        lower = middle + 1
        if lower > upper and '>' in inequality:
          middle = lower

    return middle

if __name__ == "__main__":
  n = int(input())

  ducks = input().split()
  ducks = [int(i) for i in ducks]
  
  q = int(input())
  weight_queries = []
  for _ in range(q):
    row = input().split()
    row = (int(row[0]), int(row[1]))
    weight_queries.append(row)
  
  # print(', '.join([str(el) for el in ducks]))
  duck_w = DuckWeight(ducks, weight_queries)
  duck_w.find()
