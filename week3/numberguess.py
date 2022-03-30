from random import randint
# from players import Player


class Player():

  # Create a player
  def __init__(self, player_name):
    self.name = player_name
    self.score = 0
    self.guess = 0
    
  def enterGuess(self,rand, play):
    
    if play == True:
      self.guess = int(input(self.name+ " enter a guess 1-100:"))
        
      if self.guess == rand:
        print ("Correct Guess")
        play = False
        self.score = self.score + 1
            
      elif self.guess < rand:
        print ("Too low")
            
      else:
        print ("Too high")
      
      return play
  
  
  
  

#================           Set player objects        =============================

print ("Player 1")
player1=Player(input("Enter name:"))

print ("Player 1")
player2=Player(input("Enter name:"))

#==========               Play single game function     ============================

def playGame():
  randNum = randint(1,100)
  play = True
  print ("\nNew game")
  
  while play:
    play=player1.enterGuess(randNum, play)
    play=player2.enterGuess(randNum, play)
  
  print ("\nScore: "+player1.name+" "+str(player1.score)+" | "+player2.name+" "+str(player2.score))
  
#=====================       Game play section               ===============================

quit = False
while quit != True:
  playGame()
  keepPlaying=input("\nDo you want to quit (y/n): ")
  if keepPlaying == "y":
    quit = True
    
print ("\nFinal Score: "+player1.name+" "+str(player1.score)+" | "+player2.name+" "+str(player2.score))   
  