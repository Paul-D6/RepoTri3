# Paul DiPasquale
## Notes
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
- - One benefit is that people cand find ways to automate aspects of life using programs. The harm in this is that people will become lazy and rely on computers to do everything for them.
- - A benefit is that communication is faster and more efficient between devices. The harm in this is that people will be more likely to use digital communication rather than in person interaction.
- - I think that dopamine issues are very real, especially for high school students with heavy work loads. Students may be more inclined to relax and give themselves some down time in between assignments than to focus and get their work done. I am distracted by YouTube and other platforms on my phone when trying to do my homework sometimes, which makes it take longer. It is a problem that probably many people face, and we need to learn to overcome it.
- 5.2
- - To empower yourself in the digital world, one must be willing to use technology in useful, innovative ways. Utilizing their skills to solve problems and benefit others is a great example of what makes someone empowered. Being empowered in the digital world also requires someone to have access to technology and internet services, and due to the digital divide, not everyone does.
- - An empowered person can help a non-empowered person by helping them solve problems that they would not normally be able to address. At DNHS, something I could do is build a website that benefits a group of people that may not be able to create one themselves.
- - I think paper and red tape does contribute to blocking digital empowerment. At Del Norte, for example, certain websites are blocked by the school wifi (“red tape”). This blocks potentially useful sites, which could prevent certain classes from being digitally empowered. Paper is also used in some of my classes mainly, which prevents the classes from advancing technologically and becoming digitally empowered.

##Replit

##### [Website](https://replit.com/@PaulDiPasquale/algorithms#main.py)
https://replit.com/@PaulDiPasquale/RepoTri3#main.py
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@PaulDiPasquale/RepoTri3#main.py?embed=true"></iframe>


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
