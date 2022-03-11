def main():
  stars = 1
  numspace = 5

  while stars < 7:
    space = " " * numspace
    row = "* " * stars
    print(space + row)
    stars += 1
    numspace -= 1
  print((" " * 4)+("*" * 3))
  print((" " * 4)+("*" * 3))

if __name__ == "__main__":
    main()