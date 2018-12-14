import list

def menu():
    os.system('cls')
    print ("Select option:\n")
    print("1 - New user\n")
    print("2 - Delete user\n")
    print("3 - Show users\n")
    print("4 - Add Assists\n")
    print("9 - Exit")


while True:
    menu()
    optionMenu = input("Insert value >> ")
    if optionMenu == "1":
        print("")
        input("Has pulsado la opción 1...\n")
        list.newUser()
    elif optionMenu == "2":
        print("")
        input("Has pulsado la opción 2...\n")
        list.deleteUser()
    elif optionMenu == "3":
        print("")
        input("Has pulsado la opción 3...\n")
        list.showUser()
    elif optionMenu == "4":
        print("")
        input("Has pulsado la opción 4...\n")
       # asssist()
    elif optionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


