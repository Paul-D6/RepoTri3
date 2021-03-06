# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# abstracted files in a folder (aka module)

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
from week0 import animate
from week0 import matrix
from week0 import swap
from week0 import tree
from week1 import datalists
from week1 import fibonacci
from week2 import factorial
from week2 import mathfunc
from week2 import palindrome
from week3 import clear

main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu1 = [
  ["Lists&Loops", datalists.main],
]
sub_menu2 = [
  ["Matrix", matrix.matrix],
  ["Swap", swap.swap],
  ["Fibonacci", fibonacci.main],
  ["MathFunc", mathfunc.main],
  ["Factorial", factorial.main],
]
sub_menu3 = [
  ["Tree", tree.main],
  ["Animation", animate.main],
  ["Palidrome", palindrome.main],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["\u001b[32;1mData\u001b[0m", submenu1])
    menu_list.append(["\u001b[35;1mMath\u001b[37;1m", submenu2])
    menu_list.append(["\u001b[36;1mAdventure\u001b[37;1m", submenu3])
    # menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu1():
    title = "Data" + banner
    buildMenu(title, sub_menu1)
def submenu2():
    title = "Math" + banner
    buildMenu(title, sub_menu2)
def submenu3():
    title = "Adventure" + banner
    buildMenu(title, sub_menu3)

  
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["\u001b[31mExit\u001b[37m", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")
    clear.clearConsole()

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
