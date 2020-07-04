import Menu
def AppendFile():
      print("\f")
      print("~~~~Append Data to the Player File~~~~")
      Filename = input("Enter the Player ID to Append Details: ")
      Data = input("Enter Data to append: ")

      File = open(Filename, 'a')
      File.write("\n%s" % (Data))

      File.close()
      print("~~~~Record Appended to ",Filename, "Player~~~~")
      Menu.MainMenu()
