def main():
  stars = 1
  numspace = 5
## starts the values for the spaces and stars
  while stars < 7:
    space = " " * numspace
    row = "* " * stars
    print(space + row)
    ## prints the layer
    stars += 1
    numspace -= 1
    ## adds or subtracts variables
  print((" " * 4)+("*" * 3))
  print((" " * 4)+("*" * 3))

if __name__ == "__main__":
    main()