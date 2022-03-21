{% include navbar.html %}

## Replit

##### [Website](https://replit.com/@PaulDiPasquale/RepoTri3#main.py)


{% include replit.html %}


#### Menu Bar
- This is my menu bar where I added all my functions from different files of my replit
- There is also a submenu that will access the code from a file called "Challenges"

```
main_menu = [
  ["Swap", "swap.py"],
  ["Matrix", "matrix.py"],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
  ["Christmas Tree", tree.main],
  ["Animation", animate.main]
]
```

#### Tree function
- In this function, I used a a loop to print out each layer of the tree, they. all had a different format so I had to change variables as I went trhough the loop.
- There was a different number of spaces of and stars that were changed throughout the function

```
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
   ```

### Loops and List printing
- This function outputs multiple loops in different ways as it takes the data in the lists
```
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return
```

### Fibonacci
- This function uses a user input to add numbers and create and out put. This is done using multiple funcitons and a loop.
```
def calc_series(self):
        limit = self._series
        f = [0, 1]  # fibonacci starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], f[0] + f[1]]
            limit -= 1

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1
```