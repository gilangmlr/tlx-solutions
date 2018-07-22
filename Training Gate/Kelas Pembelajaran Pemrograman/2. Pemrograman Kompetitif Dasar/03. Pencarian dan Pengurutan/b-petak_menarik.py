from operator import itemgetter

class InterestingBoard:
  def __init__(self, _board, _interesting_target):
    self.board = _board
    self.row_size = len(_board)
    self.col_size = len(_board[0])
    self.i_target = _interesting_target
  
  def play(self):
    i_results = []
    for i in range(self.row_size):
      for j in range(self.col_size):
        if self.interesting_value(i, j) == self.i_target:
          i_results.append((i + 1, j + 1))
    
    if len(i_results) == 0:
      print('0 0')
    elif len(i_results) == 1:
      row, col = i_results[0]
      print('{} {}'.format(row, col))
    else:
      sorted_i_results = sorted(i_results, key=itemgetter(1,0))
      row, col = sorted_i_results[0]
      print('{} {}'.format(row, col))


  
  def interesting_value(self, row, col):
    i_values = []
    if row > 0:
      i_value = self.board[row - 1][col]
      i_values.append(i_value)
    if col < self.col_size - 1:
      i_value = self.board[row][col + 1]
      i_values.append(i_value)
    if row < self.row_size - 1:
      i_value = self.board[row + 1][col]
      i_values.append(i_value)
    if col > 0:
      i_value = self.board[row][col - 1]
      i_values.append(i_value)
    
    i_value = 1
    for i_val in i_values:
      i_value *= i_val
    return i_value

if __name__ == "__main__":
  n, m, k = input().split()
  n = int(n)
  m = int(m)
  k = int(k)

  board = []
  for _ in range(n):
    row = input().split()
    row = [int(i) for i in row]
    board.append(row)
  
  i_board = InterestingBoard(board, k)
  i_board.play()
