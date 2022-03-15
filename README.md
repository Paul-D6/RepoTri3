{% navbar.html %}


# Paul DiPasquale
##### [Link to Github page](https://paul-d6.github.io/RepoTri3/)

{% include navbar.html %}


## Notess
### 5.1
- People create computing innovations
- The way people complete tasks often changes to incorporate new computing innovations
- Not every effect of a computing innovation is anticipated in advance
- A single effect can be viewed as both beneficial and harmful by different people or even by the same person
- Advances in computing have generated and increased creativity in other fields, such as medicine, engineering, communications and the arts
- Computing innovations can be used in ways that their creators had not originally intended
- The World Wide Web was originally intended only for rapid and easy exchange of information within the scientific community
- Targeted advertising is used to help businesses but can be misused at both individual and aggregate levels
- Machine learning and data mining have enabled innovation in medicine, business, and science, but information discovered in this way has also been used to discriminate against groups of individuals
- Some of the ways computing innovations can be used may have a  harmful impact on society, the economy or culture

### 5.2
- A decidable problem is a decision problem for which an algorithm can be written to produce a correct output for all inputs
- An undecidable problem is one for which no algorithm can be constructed that is always capable of providing a correct yes-or-no answer.
- An undecidable problem may have some instances that have an algorithmic solution, but there is no algorithmic solution that could solve all instances of the problem
### Question Responses
- 5.1
- - A benefit is people can use computers to supplement life skills so they will not have to do it. The downside in this is, is that people will become reliant on computers and some people might loose their job.
- - A benefit is that communication is a lot faster which allows people to be updated in a short amount of time. The negative affect on this is people will be more likely to stop the traditional, personal interaction and prefer to communicate digitally.
- - I would say that dopamine issues are very real, especially for people that have a lot of work. These people would rather give themselves more breaks in between assignments than to focus and get their work done. I am personally distracted with social media and other applications on my phone when trying to get my work done sometimes It is a serious problem that almost everyone faces, and could affect the amount of time something gets done.
- 5.2
- - To empower yourself in the digital world, it is ideal to use technology in innovative ways. By using their skills to solve problems and benefit others, it is a great example of what makes someone empowered. Being empowered in the digital world also requires someone to have access to technology and internet services, and due to the digital divide, not everyone does.
- - An empowered person can help a non-empowered person by helping them solve problems that they would originally not be able to solve. For example, I could build a website or platform that benefits a people in a way that people. could not have. done. before.
- - I think paper and red tape does contribute to blocking digital empowerment. At school, there are certain websites that are blocked by the wifi (“red tape”). The websites could potentially be usefull and they prevent certain classes from being digitally empowered. Paper is also used in certain feilds of study, which prevents the classes from becoming digitally empowered.

## Replit

##### [Website](https://replit.com/@PaulDiPasquale/algorithms#main.py)
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@PaulDiPasquale/RepoTri3?embed=true" >


Menu Bar
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

Tree function
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
    
## Create Task
- Planning
- - Idea is still being determined
- Responses
- - [x] Instructions for input: User will be able to select whether or not they would like to add a book to their wishlist. There will be 5 options to choose from that the user will decide on
- - [x] Use of at least 1 list: The books that will be prompted will be from a question list. A list will also be created as the user decides on the books that they like.(push-js)
- - [x] At least 1 procedure: The procedure will be taking the input from a user and the function will produce a list of books that they wanted to add to their wishlist
- - [x] An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure: The function runs through a loop that adds questions to a list and shuffles them. There will be different parts to this and only certain action will occur when  specific conditions are met. Ex: If the user likes the book, the function will add it to a list.
- - [x] Calls to your student-developed procedure: the "next" button will switch to different question and allow the user to decide on the next book they want to add
- - [x] Instructions for output (tactile, audible, visual, or textual) based on input program functionality: The output will be a textual list of books that the user created
