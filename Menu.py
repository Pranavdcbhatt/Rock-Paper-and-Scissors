import sys
import Create
import View
import Append
import Delete
import Game

def MainMenu():
    print("Enter 1 to Create a Game file manually")
    print("Enter 2 to Edit a Game file")
    print("Enter 3 to View a Game file")
    print("Enter 4 to Delete a Game file")
    print("Enter 5 to play a game and create it's file")
    print("Enter 0 to Exit")
    choice = int(input("Please enter now: "))
    if(choice ==1):
        Create.CreateFile()
    elif(choice==2):
        Append.AppendFile()
    elif(choice==3):
        View.ViewFile()
    elif(choice==4):
        Delete.DeleteFile()
    elif(choice==5):
        Game.GAME()
    elif(choice==0):
        print("Have a great day!!")
        sys.exit(0)
    else:
        print('\f')
        print("It seems your input was not according to our references. Please view the choices again")
        return
