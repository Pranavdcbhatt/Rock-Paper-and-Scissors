import Menu
import os
def DeleteFile():
      print("\f")
      File = input("Enter Player ID to delete: ")
      if os.path.exists(File):
            os.remove(File)
            print("File ",File," deleted")
      else:
            print("Sorry, %s Not found" %File)
      Menu.MainMenu()
