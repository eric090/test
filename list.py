import os
import pickle



#list_names = ['Otger B.', 'Juan B.', 'Laia C.', 'Jorge G.', 'Alex G.', 'Pepe I.', 'Jorge J.', 'Oscar M.', 'Julià M.', 'Eric P.', 'Cristobal P.', 'David R.', 'Marti V.']
#names = {'Names': list_names}
data = []
def newfile():
    F = open('names.pkl', 'wb')
    F.close()
    print("File created")

def newUser(name):
    os.system('cls')
    a = {'name' : name}
    data.append(a)
    print(len(data))
    #list_names.append(a)
    F = open('names.pkl', 'wb')
    pickle.dump(data,F)

    F.close()
def deleteUser(name):
    os.system('cls')
    delete_name = {'name': name}
    error = True

    for x in range(0, len(data)):
        if delete_name == data[x]:
            data.pop("name", name)
            F = open('names.pkl', 'wb')
            pickle.dump(data, F)
            F.close()
            print("Name delet1ed succes")
            error = False
    if error:
        print("Name incorrect, please enter the name again")
        deleteUser(delete_name)

def showList():
    os.system('cls')
    e = open('names.pkl','rb')
    print(pickle.load(e))


def add_assist(name):
    F = open('names.pkl', 'wb')
    list_names = F
    for i in list_names:
        if name == list_names[i]:
            list_names[i]["assist: "] +=1

