def random():
  import random
  random_number = random.randint(1,100)
  win = False #to make sure player starts in the loops
  Turns = 0 #set turn counter to 0
  
 #starts loop of guessing
  while win==False:
    wrong = False
    while not wrong:
      try:
        Guess = input("Guess a whole number between 1 and 100: ")
        Guess = int(Guess)
        wrong = True
      except:
        wrong = False
        print("Invalid input.")
      
    

    Turns += 1 #tracks turns
    print("Turns:", Turns ,"out of 10")
    if Turns==10:
      print("10 turns up, you lose.")
      return #ends loop
    elif random_number==Guess: #ends loop if player wins
      print("You win!")
      print("Number of turns used:", Turns , "out of 10")
      win = True
    elif random_number >=Guess: #tells player if a guess is too high or low
        print("Your guess was too low. Aim higher.")
    else:
        print("Your guess was too high. Aim lower.")
  
    
    if Guess<=0:
      print(f"{Guess} is not in between the boundaries.")
    if Guess>100:
      print(f"{Guess} is not in between the boundaries.")
