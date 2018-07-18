if __name__ == "__main__":
  pattern = input()
  number_of_strings = int(input())

  for index in range(0, number_of_strings):
    word = str(input())
    patlist = pattern.split('*')
    if word.startswith(patlist[0]) and word.endswith(patlist[1]) and len(word) >= (len(patlist[0]) + len(patlist[1])):
      print(word)