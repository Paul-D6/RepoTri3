def swap():
  def change(first, second):
    save = first
    first = second
    second = save
    return first, second
  while True:
    age1 = 11
    age2 = 7
    print(age1,age2)
    if age1 > age2:
      print(change(age1, age2))
    break
  
if __name__ == "__main__":
    swap()