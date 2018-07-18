class Runtuh:
  def __init__(self, _blocks):
    self.blocks = _blocks
    self.number_of_row = len(self.blocks)
    self.number_of_column = len(self.blocks[0]) if self.number_of_row > 0 else 0
    self.last_hapus_row = 0
  
  def play(self):
    while self.hapus():
      self.runtuh()
    self.print_blocks()

  @staticmethod
  def print_blocks_static(blocks):    
    for row in blocks:
      print(''.join([str(el) for el in row]))
  
  def print_blocks(self):
    for row in self.blocks:
      print(''.join([str(el) for el in row]))
  
  def hapus(self):
    anyFull = False
    for index_of_row, row in enumerate(self.blocks):
      isFullRow = True
      for element in row:
        if element == 0:
          isFullRow = False

      if isFullRow:
        anyFull = True
        self.last_hapus_row = index_of_row
        for index_of_column, element in enumerate(row):
          row[index_of_column] = 0
    return anyFull
  
  def runtuh(self):
    for index_of_column in range(0, self.number_of_column):
      last_runtuh_row = self.last_hapus_row
      for index_of_row in range(self.last_hapus_row + 1, self.number_of_row):
        if self.blocks[index_of_row][index_of_column] == 1 or index_of_row == self.number_of_row - 1:
          last_runtuh_row = index_of_row
          break
      number_of_ones = 0
      for index_of_row in range(0, last_runtuh_row + 1):
        if self.blocks[index_of_row][index_of_column] == 1:
          self.blocks[index_of_row][index_of_column] = 0
          number_of_ones += 1
        self.blocks[index_of_row][index_of_column] == 0
      for index_of_row in range(last_runtuh_row, last_runtuh_row - number_of_ones, -1):
        self.blocks[index_of_row][index_of_column] = 1


if __name__ == "__main__":
  tmp = input().split()
  number_of_row = int(tmp[0])
  number_of_column = int(tmp[1])

  blocks = []
  for row_index in range(0, number_of_row):
    tmp = list(input())
    row = []
    for column_index in range(0, number_of_column):
      row.append(int(tmp[column_index]))
    blocks.append(row)

  game = Runtuh(blocks)

  game.play()