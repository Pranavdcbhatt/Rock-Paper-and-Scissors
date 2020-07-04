import Menu
def CreateFile():
    print("\f")
    print("~~Create a Game File~~")
    playerName = input("Enter the name of the Player:")
    playername = "Player Name = "+playerName
    date = input("Enter the date of the game played: ")
    date = "Date: "+date
    pscore = float(input("Enter the player's score: "))
    score1 = pscore
    pscore = str(pscore)
    pscore = "Player's score: "+pscore
    cscore = float(input("Enter the Computers' score: "))
    score2 = cscore
    cscore = str(cscore)
    cscore = "Computer's score: "+cscore
    with open(playerName, 'w') as File:
        File.write('%s\n%s\n%s\n%s' %(playername, date, pscore, cscore))
        File.close()
    print("~~Game File" ,playerName," Created~~")
    Menu.MainMenu()
        
    
    
