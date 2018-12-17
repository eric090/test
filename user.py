import os
import pickle



#list_names = ['Otger B.', 'Juan B.', 'Laia C.', 'Jorge G.', 'Alex G.', 'Pepe I.', 'Jorge J.', 'Oscar M.', 'Julià M.', 'Eric P.', 'Cristobal P.', 'David R.', 'Marti V.']
#names = {'Names': list_names}
data = []

def newfile():
    F = open('names.pkl', 'wb')
    F.close()
    print("File created")

def newUser(name, point):
    os.system('cls')
    a = {'name': name, 'points': point}
    data.append(a)
    print(len(data))
    #list_names.append(a)
    F = open('names.pkl', 'wb')
    pickle.dump(data,F)

    F.close()
def deleteUser(name):
    os.system('cls')
    error = True
    print("delete user: " + name)
    for value in data:
        if name == value["name"]:
            data.remove(value)
            F = open('names.pkl', 'wb')
            pickle.dump(data, F)
            F.close()
            print("Name deleted successfully")
            error = False
    if error:
        print("Name incorrect, please enter the name again")

def showList():
    os.system('cls')
    e = open('names.pkl','rb')
    print(pickle.load(e))


def add_assist(name):
    os.system('cls')
    error = True
    print("add point to: " + name)
    for value in data:
        if name == value["name"]:
            data[value]['points'] += 1
            F = open('names.pkl', 'wb')
            pickle.dump(data, F)
            F.close()
            print("Point added successfully")
            error = False
    if error:
        print("Name incorrect, please enter the name again")







