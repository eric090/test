import user
import os.path
from user import newUser
DEFAULT_POINT = 1
DEFAULT_ATTENDANCE = 1

if os.path.isfile('names.pkl'):
    print("File already exist")
else:
    user.newfile()

def main():
    print ("Select option:\n")
    print("1 - New user\n")
    print("2 - Delete user\n")
    print("3 - Show users\n")
    print("4 - Add Attendance\n")
    print("5 - Add point")
    print("6 - Show information ")
    print("7 - Who clean? ")
    print("9 - Exit")
newUser("Paco", DEFAULT_ATTENDANCE, DEFAULT_POINT)
newUser("pepe", DEFAULT_ATTENDANCE, DEFAULT_POINT)
newUser("Alex", DEFAULT_ATTENDANCE, DEFAULT_POINT)
newUser("Joan", DEFAULT_ATTENDANCE, DEFAULT_POINT)
newUser("cristobal", DEFAULT_ATTENDANCE, DEFAULT_POINT)
while True:
    main()
    optionMenu = input("Insert value >> ")
    if optionMenu == "1":
        print("")
        print("Has pulsado la opción 1...\n")
        name = input("Insert name: ")

        user.newUser(name, DEFAULT_ATTENDANCE, DEFAULT_POINT)
    elif optionMenu == "2":
        print("")
        print("Has pulsado la opción 2...\n")
        name = input("Insert name: ")
        user.deleteUser(name)
    elif optionMenu == "3":
        print("")
        print("Has pulsado la opción 3...\n")
        user.showList()
    elif optionMenu == "4":
        print("")
        print("Has pulsado la opción 4...\n")
        name = input("Insert name: ")
        user.addAttendance(name)
    elif optionMenu == "5":
        print("")
        print("Has pulsado la opción 5...\n")
        name = input("Insert name: ")
        user.addPoint(name)
    elif optionMenu == "6":
        print("")
        print("Has pulsado la opción 6...\n")
        user.getParameters()
    elif optionMenu == "7":
        print("")
        print("Has pulsado la opción 7...\n")
        user.getName()
    elif optionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


