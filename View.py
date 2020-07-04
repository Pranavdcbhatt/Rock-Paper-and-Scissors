import Menu

def ViewFile():
    print("\f")
    print("~~View Game File~~")
    playername = input("Enter File Name or the Name of the player: ")
    File = open(playername, 'r')
    content = File.read()
    print(content)
    File.close()
    print("~~End of File for Player ",playername,"~~")
    Menu.MainMenu()
        
