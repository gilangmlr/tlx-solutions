from operator import itemgetter

class YellowBook:
  def __init__(self, _book, _name_queries):
    self.book = _book
    self.name_queries = _name_queries
  
  def find(self):
    for name in self.name_queries:
      print(self.binary_search(name))

  def binary_search(self, name):
    lower = 0
    upper = len(self.book) - 1

    while lower <= upper:
      middle = (upper + lower) // 2
      name_middle = self.book[middle][0]
      phone_middle = self.book[middle][1]
      if name_middle == name:
        return phone_middle
      elif name < name_middle:
        upper = middle - 1
      else:
        lower = middle + 1
    
    return 'NIHIL'

if __name__ == "__main__":
  n, q = input().split()
  n = int(n)
  q = int(q)

  book = []
  for _ in range(n):
    row = input().split()
    row = (str(row[0]), str(row[1]))
    book.append(row)
  
  name_queries = []
  for _ in range(q):
    row = input()
    name_queries.append(row)
  
  y_book = YellowBook(book, name_queries)
  y_book.find()
