import list
import os.path

if os.path.isfile('names.pkl'):
    print("File already exist")
else:
    list.newfile()

def main():
    print ("Select option:\n")
    print("1 - New user\n")
    print("2 - Delete user\n")
    print("3 - Show users\n")
    print("4 - Add Assists\n")
    print("9 - Exit")
while True:
    main()
    optionMenu = input("Insert value >> ")
    if optionMenu == "1":
        print("")
        print("Has pulsado la opción 1...\n")
        name = input("Insert name: ")
        list.newUser(name)
    elif optionMenu == "2":
        print("")
        print("Has pulsado la opción 2...\n")
        name = input("Insert name: ")
        list.deleteUser(name)
    elif optionMenu == "3":
        print("")
        print("Has pulsado la opción 3...\n")
        list.showList()
    elif optionMenu == "4":
        print("")
        print("Has pulsado la opción 4...\n")
        name = input("Insert name: ")
        list.add_assist(name)
       # asssist()
    elif optionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


