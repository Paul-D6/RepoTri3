{% include navbar.html %}

## Replit

##### [Website](https://replit.com/@PaulDiPasquale/RepoTri3#main.py)

##### Replit at bottom of page


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

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@PaulDiPasquale/RepoTri3?embed=true" >
