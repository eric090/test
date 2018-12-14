import os
import pickle

PICKLE_FILE = "names.pkl"
list_names = ['Otger B.', 'Juan B.', 'Laia C.', 'Jorge G.', 'Alex G.', 'Pepe I.', 'Jorge J.', 'Oscar M.', 'Julià M.', 'Eric P.', 'Cristobal P.', 'David R.', 'Marti V.']
names = {'Names': list_names}

list_assist = [len(list_names)]
list_clean = [len(list_names)]

F = open('names.pkl','wb')
pickle.dump(names,F)
F.close()

def newUser():
    os.system('cls')
    new_name = input("Insert name: ")
    list_names.append(new_name)
    names = {'Names': list_names}
    F = open('names.pkl', 'wb')
    pickle.dump(names, F)
    F.close()
    menu()
def deleteUser():
    os.system('cls')
    deletename = input("Insert name: ")
    error = True
    for x in range (0, len(list_names)):
        if deletename == list_names[x]:
            list_names.pop(x)
            names = {'Names': list_names}
            F = open('names.pkl', 'wb')
            pickle.dump(names, F)
            F.close()
            print("Name deleted succes")
            error = False
    if error:
        print("Name incorrect, please enter the name again")
        deleteUser()

def showUser():
    os.system('cls')

    e = open('names.pkl','rb')
    print(pickle.load(e))
    #for item in read_from_pickle(PICKLE_FILE):

    #os.remove(PICKLE_FILE)

def add_to_pickle(path, item):
    with open(path, 'ab') as file:
        pickle.dump(item, file, pickle.HIGHEST_PROTOCOL)
def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass
