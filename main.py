# I got the file thing to work, turns out it was just the dictionary problem
# All you have to do to call the file is:
# import <filename>
# <filename>.main()

""""
import sys
menu = print("What game would you like to play?:")
print("1: Hangman")
print("2: Guessing Game")
print("3: Exit")
answer = input("Enter a number: ")

if answer==1:
  def hangmany():
    import hangmany
    hangmany.game()
  hangmany()

if answer==2:
  def guess():
    import guess
    guess.random()
  guess()

if answer==3:
  sys.exit()
"""


def hangmany():
  import hangmany
  hangmany.game()
  
def guess():
  import guess
  guess.random()

func_dict = {
  1: hangmany, 
  2: guess, 
}
def menu():
  print()
  print("="*35)
  print("What game would you like to play?:")
  print("="*35)
  mylist = ["0) Exit","1) Hangman","2) Guessing Game"]
  for x in mylist:
    print(x)

  choice = input("Type a number: ")
  
  try:
    choice = int(choice)
    if choice==0:
      return
    exe_func = func_dict.get(choice)
    exe_func()
  except ValueError: 
    print(f"{choice} is not a number")
  except:
    print(f"{choice} is an invalid choice")
  menu()

menu()
print("You have exited")