import Menu
import random
def GAME():
    global name
    name = input("Please enter your name: ")
    global date
    date = input("Please enter today's date: ")
    global limit
    limit = int(input("Enter the limit of points you want to play the Game of: "))
    global ppoint, cpoint
    ppoint = 0
    cpoint = 0
    while ppoint<limit and cpoint<limit:
        print("Enter 'Rock' to choose Rock")
        print("Enter 'Paper' to choose Paper")
        print("Enter 'Scissors' to choose Scissors")
        pchoice = input("Enter your choice: ")
        cchoices = ("Rock" , "Paper", "Scissors", "Sorry, I got carried away with my calculations. Let me try Again!")
        cchoice = random.choice(cchoices)
        print("You chose: ",pchoice)
        print("Computer: ",cchoice)
    
                
        if pchoice == "Rock" and cchoice == "Rock":
            print("You've got a thought process like that of a Computer!!")
            print("Let's Try Again")
            ppoint+=0.5
            cpoint+=0.5
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
                
        elif pchoice == "Rock" and cchoice == "Paper":
            print("The Computer has won this Round!")
            print("Let's Try Again!!")
            cpoint+=1
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
            
        elif pchoice == "Rock" and cchoice == "Scissors":
            print("You have won this Round!!")
            print("Let's Go Again!!")
            ppoint+=1
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
            
                
        elif pchoice == "Paper" and cchoice == "Rock":
            print("You have Won this Round!!")
            print("Let's Do It Again")
            ppoint+=1
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
                
        elif pchoice == "Paper" and cchoice == "Paper":
            print("You've got a thought process like that of a Computer!!")
            print("Let's Try Again")
            ppoint+=0.5
            cpoint+=0.5
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
                
        elif pchoice == "Paper" and cchoice == "Scissors":
            print("The Computer has Won this Round!")
            print("Let's Try Again")
            cpoint+=1
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
               
        elif pchoice == "Scissors" and cchoice == "Rock":
            print("The Computer has won this time!!")
            print("Let's Try Again")
            cpoint+=1
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
            
        elif pchoice == "Scissors" and cchoice == "Paper":
            print("You have cut right through the Computer's intensions of winning this round!!")
            print("Well Done!!")
            print("Once More!!")
            ppoint+=1
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)

        elif pchoice == "Scissors" and cchoice == "Scissors":
            print("You've got a thought process like that of a Computer!!")
            print("Let's Try Again")
            ppoint+=0.5
            cpoint+=0.5
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)

        elif (pchoice == "Rock" and cchoice == "Sorry, I got carried away with my calculations. Let me try Again!") or (pchoice == "Paper" and cchoice == "Sorry, I got carried away with my calculations. Let me try Again!") or (pchoice == "Scissors" and cchoice == "Sorry, I got carried away with my calculations. Let me try Again!"):
            print("Hehe! It seems like even the Computer is getting nervous to play against a smart person like you")
            print("Let's Go Again!")
            ppoint+=0.5
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)

        else:
            print("It seems your Input was wrong")
            print("Please try again!")
            cpoint+=0.5
            print("Your Score: ",ppoint)
            print("Copmuter's Score: ",cpoint)
            print("Game Over")
    if ppoint>cpoint:
        print("You have won the game!")
    elif ppoint<cpoint:
        print("The Computer won the game! Better luck next time!")
    elif ppoint==cpoint:
        print("It seems that you have drawn against the Computer as you are as smart as the Computer itself!")
    print("Enter 1 if you want to Create a File for the game you just played")
    print("Enter 2 if you want to go back to the Main Menu")
    print("Enter 3 if you want to Exit")
    choice = int(input("Please Enter now: "))
    if choice==1:
        Create(ppoint, cpoint)
    elif choice==2:
        Menu.MainMenu()
    elif choice==3:
        print("Thank you and have a great day!!")
        sys.exit(0)
    else:
        print("Your choice was not according to our references.")
        print("Your File will be created by default by the name ",name,". You may view, edit or delete it via the Main Menu")
        Default(ppoint,cpoint)

def Create(ppoint,cpoint):
    print("Enter 1 if you want to Manually create the Game file")
    print("Enter 2 if you want to create the Game File by default standard")
    choice = int(input("Please enter your choice: "))
    if choice==1:
        Manually(ppoint, cpoint)
    elif choice==2:
        Default(ppoint, cpoint)
    else:
        print("It seems that your input was not according to our references. We will create the Game file by default standards by the name ",name,".")
        print("You may view, edit or delete this file via the Main Menu")
        Default(ppoint, cpoint)

def Manually(ppoint,cpoint):
    print("~~Create a Game File~~")
    playerName = input("Enter the name of the Player:")
    playername = "Player Name = "+playerName
    date = input("Enter the date of the game played: ")
    date = "Date: "+date
    pscore1 = float(input("Enter the player's score: "))
    score1 = pscore1
    pscore1 = str(pscore1)
    pscore1 = "Player's score: "+pscore1
    cscore1 = float(input("Enter the Computers' score: "))
    score2 = cscore1
    cscore1 = str(cscore1)
    cscore1 = "Computer's score: "+cscore1
    winner = input("Enter who was the winner of this game: ")
    winner = "Winner : "+winner
    with open(playerName, 'w') as File:
        File.write('%s\n%s\n%s\n%s\n%s' %(playername, date, pscore1, cscore1,winner))
        File.close()
    print("~~Game File" ,playerName," Created~~")
    Menu.MainMenu()

def Default(ppoint, cpoint):
    playerName = name
    playername = "Player Name = "+playerName
    gamedate = date
    gamedate = "Date: "+date
    score1 = ppoint
    ppoint = str(ppoint)
    ppoint = "Player's score: "+ppoint
    score2 = cpoint
    cpoint = str(cpoint)
    cpoint = "Computer's score: "+cpoint
    if score1>score2:
        winner = "Winner: "+name
    elif score2>score1:
        winner = "Winner: Computer"
    with open(playerName, 'w') as File:
        File.write('%s\n%s\n%s\n%s\n%s' %(playername, date, score1, score2,winner))
        File.close()
    print("~~Game File" ,playerName," Created~~")
    Menu.MainMenu()
