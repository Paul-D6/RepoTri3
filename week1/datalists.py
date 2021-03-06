
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Paul",  
               "LastName": "DiPasquale",  
               "DOB": "January 3",  
               "Residence": "San Diego",  
               "Email": "pauld39403@powayusd.com",  
               "Owns_Cars":["2015 Fusion","2011 Ranger","2003 Excursion","1997 F-350", "1969 Cadillac"]  
              })  

InfoDb.append({  
               "FirstName": "Jack",  
               "LastName": "Smith",  
               "DOB": "July 5",  
               "Residence": "San Diego",  
               "Email": "jacks83025@powayusd.com",  
               "Owns_Cars":["A","B","C"]  
              })  
# for loop iterates on length of InfoDb
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()
  
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

def main():
  print("For loop")
  for_loop()
  print("While loop")
  while_loop(0)
  print("Recursive loop")
  recursive_loop(0)



if __name__ == "__main__":
    main()