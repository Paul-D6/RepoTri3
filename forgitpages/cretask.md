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
- [Video](https://www.youtube.com/watch?v=TzYFZ9aklUA)


# Create Task Written Responses

Part A:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | Describe the overall purpose of the program | The purpose of the program is to provide the user a list of tasks based on the amount of time they have. It will randomly choose these tasks and display them in list|
ii | Describe what part of the program is being shown in the video |  |
iii | Describes the input and output of the program demonstrated in the video | |

Part B:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | The first program code segment must show how data have been stored in the list. | ```tasklist = {'Laundry':2,'Clean Fridge':1,'Mow Lawn':3,'Clean dishes':1,'Paint walls':4,'Buy Groceries':3,'Sweep/Mop':4,'Dust':3,'Walk Dog':2, 'Organize Desk':1} # list of tasks```|
ii | The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. | ```createlist(choice, tasklist))``` ```createlist(num, mylist): # the function``` ```task, thour = random.choice(list(mylist.items()))```|

B Sub-part iii-v
Sub-Part | Question | Answer | 
--- | -------- | --------- |
iii | Identifies the name of the list being used in this response | ```tasklist``` is the name of the dictionary being used |
iv | Describes what the data contained in the list represent in your program | The Data contained in the dictionary represents different tasks and their hours attached to them. Both of these values are used throughout the program |
v | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list | If this list was not included in the program, the program would not be able to run. This is due to the part where the list is called and uses the values to create a new list of tasks. |

Part C:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration | Shown Below |
```
def createlist(num, mylist):
  hours = 0
  finlist = []
  while hours != num:
    task, thour = random.choice(list(mylist.items()))
    space = num - hours # Amount of hours that can still be added to list
    if thour <= space and task not in finlist: # don't repeat tasks
      if thour >= 2 and space >= 2: # Prioritizes over tasks that take longer so the "1"s can fill in the rest
        finlist.append(task)
        hours += thour
      if thour == 1 and space <= 3:
        finlist.append(task + "(Quick)")
        hours += thour
  return finlist
```
ii | The second program code segment must show where your student-developed procedure is being called in your program | Runs the function with its own specific parameter! Example Down Below |
```
main():
....other code....
  if 1 <= choice <= 24 :
    print("Your list: ", createlist(choice, tasklist))
  else:
    print("Please select a number 1-8\n\n")
    main()
```
C Sub-part iii & iv
Sub-Part | Question | Answer | 
--- | -------- | --------- |
iii |  Describes in general what the identified procedure does and how it contributes to the overall functionality of the program| This procedure returns a list of tasks based off its parameter given. The function is called when the user inputs an integer in a specific range. The function will use the list and user input to return a list of tasks..|
iv | Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. | The algorithm runs a loop of finding random tasks in the list provided and adding them to a new list if it can. It starts off by identifying the name and value of the randomly selected element in the list. It then calculates the amount of hours that are available in the new list. If the chosen task has a value too large for this calculation or the task was already added to the new list, the loop runs again. Once these conditions are met, the program prioritizes over the larger valued tasks first it can use the smaller tasks to fill in any extra time. These conditions include how large the value is, and how many hours are left in the new list(Calculation mentioned earlier). The loop will stop once the hours are filled up and a new list is created.|

Part D:
Sub-Part | Question | Answer | 
--- | -------- | --------- |
i | Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. | Condition 1: ```if thour >= 2 and space >= 2:``` Condition 2:```if thour == 1 and space <= 3:```|
ii |  Describes what condition(s) is being tested by each call to the procedure | Condition #1: The value of the randomly selected task is greater than or equal to 2 AND there is enough space(hrs) to add it into the new list.;Condition #2: The value of the randomly selected task is equal to 1 AND there is a small amount of space(hrs) to add it into the new list.|
ii | Identifies the result of each call | Result #1: If the conditions are met, the task will be added to the the new list. More space in the list will be occupied.; Result #2 If the conditions are met, the task will be added to the the new list with an extra note. A small amount of space in the list will be occupied.; |