def game():
  # Define Clear Screen Variables (Rivan)
  ANSI_CLEAR_SCREEN = u"\u001B[2J"
  ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
  
  # Obtaining user input, creating the hangmen boards (Charlie, Rivan, Rohan)
  user1 = input("Your name: ")
  user2 = input("Your friend's name: ")

  empty = """
    +---+
          |
          |
          |
          |
          |
  =========
  """
  rope =  """
    +---+
      |   |
          |
          |
          |
          |
  =========
  """
  head = """
    +---+
      |   |
      O   |
          |
          |
          |
  =========
  """
  torso = """
    +---+
      |   |
      O   |
      |   |
          |
          |
  =========

  """
  arm1 = """
    +---+
      |   |
      O   |
      |\  |
          |
          |
  =========
  """
  arm2 = """
    +---+
      |   |
      O   |
     /|\  |
          |
          |
  =========
  """
  leg1 = """
    +---+
      |   |
      O   |
     /|\  |
     /    |
          |
  =========
  """
  whole = """
    +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
  =========
  """
  
  # Printing the empty board (Rivan)
  print("Here's " + user1 + "'s board.")
  print(empty)

  # Create the line of _ 's based on the input phrase(Sarah)
  answer = input(f"{user1}, please input your phrase \n")
  key = len(answer) * '_ '

  # Keeping track of the board and whether the game has been won (Sarah)
  gameEnd = False
  man_status = 0

  # Repeat as long as the game is going (Sarah)
  while gameEnd == False:
    # Printing the board (Rivan)
    print(ANSI_HOME_CURSOR)
    print(ANSI_CLEAR_SCREEN)
    
    # Print the board based on the amount of wrong guesses (Sarah)
    if man_status == 0:
      print(rope)
    elif man_status == 1:
      print(head)
    elif man_status == 2:
      print(torso)
    elif man_status == 3:
      print(arm1)
    elif man_status == 4:
      print(arm2)
    elif man_status == 5:
      print(leg1)
    else:
      print(whole)
      gameEnd = True
      user1win = True
      break

    # Print the empty spaces (Rivan)
    print(key)

    # User2 guessing the letters (Sarah)
    c = input(f"{user2}, guess a letter: \n")

    # Make sure it's a single character (Sarah)
    while len(c) != 1:
      c = input(f"{user2},Input a single letter: ")

    # Turn the key into a list (Sarah)
    mKey = list(key.split(" ")) 

    # Check every character of the answer string (Sarah)
    index = 0
    correct = 0
    for char in answer:
      # If there's a match, update the key list (Sarah)
      if c == char:
        mKey[index] = char
        correct += 1
      index = index + 1
    # If a match hasn't been found, add another body part to the man (Sarah)
    if correct == 0:
      man_status += 1
    

    done = True
    # If there are any blank spaces left, set done to False (Sarah)
    for char in mKey:
      if char == '_':
        done = False
    
    # If there aren't any blank spaces, the game is over and user1 wins (Sarah)
    if done == True:
      gameEnd = True
      user1win = False
        

    # Join the key back into a string and print it (Sarah)
    key = ' '.join(mKey)

  # Print that the game has ended and the user that won (Rivan)
  print("the game is over")
  if user1win == False:
    print(f"{user2} wins")
    print("The word was",answer)
  else:
    print(f"{user1} wins")
    print("The word was",answer)