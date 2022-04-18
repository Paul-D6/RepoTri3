{% include navbar.html %}

## Create Task
- Planning
- - Quiz that allows user to add items into a list. The questions in the list are chosen randomly and the user decides whether they like something or not.
- Responses
- - [x] Instructions for input: User will be able to select whether or not they would like to add a book to their wishlist. There will be 5 options to choose from that the user will decide on
- - [x] Use of at least 1 list: The books that will be prompted will be from a question list. A list will also be created as the user decides on the books that they like.(push-js)
- - [x] At least 1 procedure: The procedure will be taking the input from a user and the function will produce a list of books that they wanted to add to their wishlist
- - [x] An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure: The function runs through a loop that adds questions to a list and shuffles them. There will be different parts to this and only certain action will occur when  specific conditions are met. Ex: If the user likes the book, the function will add it to a list.
- - [x] Calls to your student-developed procedure: the "next" button will switch to different question and allow the user to decide on the next book they want to add
- - [x] Instructions for output (tactile, audible, visual, or textual) based on input program functionality: The output will be a textual list of books that the user created

# Free Response questions
Part A:
Part | Question | Answer | 
|------- | -------- | ---- |
I | Describe the overall purpose of the program | The overall purpose of the program is to produce a list for the user that has the books that they like. This list can be used a reference to find books they like. |
II | Describe what part of the program is being shown in the video | The part in the program that is being shown is the the part where the input is taken and goes into whatever route it follows. It shows the conditions that have to be met for the program to go certain routes to produce an output. |
III | Describes the input and output of the program demonstrated in the video | The input that is shown is where the user chooses to either add the book to a list or not. After 5 books have been prompted, the output will show the list created for the user |

Part B:
Part | Question | Answer | 
--- | -------- | --------- |
I | The first program code segment must show how data have been stored in the list. | The list for Sci-Fi books ```sfbooks = ["Dune", "The Time Machine", "Brave New World", "The Fountain Trilogy", "Eyes of the Void"]```|
II | The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. |![image](https://cdn.discordapp.com/attachments/749509501773807677/945743260087902258/Screen_Shot_2022-02-22_at_10.05.29_AM.png)|
III | Identifies the name of the list being used in this response | ```clist``` is a parameter in the function that takes one of the lists and uses it to create a shuffled arrangement of the book category |
IV | Describes what the data contained in the list represent in your program | The data in the list represents the books being prompted to the user. It is also used to create an output of what the user has selected. |
V | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list | The lists manage the complexity of the program because it stores all the data easily without having to extract it somewhere else. This could be run by an API, although it would be difficult to categorize the genre of each book. |

Part C:
Part | Question | Answer | 
--- | -------- | --------- |
I | The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration | ![image](https://cdn.discordapp.com/attachments/749509501773807677/945741909127753758/Screen_Shot_2022-02-22_at_9.58.09_AM.png) |
II | The second program code segment must show where your student-developed procedure is being called in your program | Runs the function with its own specific parameter ![image](https://cdn.discordapp.com/attachments/749509501773807677/945741909509427200/Screen_Shot_2022-02-22_at_9.58.57_AM.png) |
III |  Describes in general what the identified procedure does and how it contributes to the overall functionality of the program| This procedure basically prompts the user with a book and the option to add it to the list or not. It starts of by taking the parameter that is chosen by the user and uses it to shuffle the books to prompt the user. It then creates the first question ```currentQuestion```. It also decides what the button "to move on" will display. |
IV | Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. | A genre is chosen in the beginning that a certain function. When this runs, it calls this other procedure that has a list for its parameter along with the starting index. When The procedure runs, it takes the chosen genre list and shuffles it to create a new list. Once the chosen list has been shuffled, the procedure will display the first question in the shuffled list. This allows the user to interact with the prompt. Once a button is clicked to go to the next question, The procedure in ran again although this time with a different index. This chosen index will choose the next question for the user. The way that this index is changed is described in Part D. |

Part D:
Part | Question | Answer | 
--- | -------- | --------- |
I | Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. | ![image](https://cdn.discordapp.com/attachments/749509501773807677/945741908720894042/Screen_Shot_2022-02-22_at_12.52.12_AM.png) |
II |  Describes what condition(s) is being tested by each call to the procedure | Condition of first: One of the options have to be selected and it the option has to be the right answer(add to wishlist); Second: One of the options have to be selected and the answer cannot be "yes"|
III | Identifies the result of each call | Result of First: If the conditions are met, the question/book will be added to the wishlist. The index of the questions will be added by 1 ; Second: Just the index of the questions will be added by 1.|