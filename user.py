import os
import pickle

data = []

def newfile():
    F = open('names.pkl', 'wb')
    F.close()
    print("File created")

def newUser(name, attendance, point):
    os.system('cls')
    a = {'name': name, 'attendance': attendance, 'points': point}
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


def addAttendance(name):
    os.system('cls')
    error = True
    print("add attendance to: " + name)
    for value in data:
        if name == value["name"]:
            value["attendance"] += 1
            F = open('names.pkl', 'wb')
            pickle.dump(data, F)
            F.close()
            print("attendance added successfully")
            error = False
    if error:
        print("Name incorrect, please enter the name again")

def addPoint(name):
    os.system('cls')
    error = True
    print("add point to: " + name)
    for value in data:
        if name == value["name"]:
            value["points"] += 1

            F = open('names.pkl', 'wb')
            pickle.dump(data, F)
            F.close()
            print("Point added successfully")
            error = False

    if error:
        print("Name incorrect, please enter the name again")
def getParameters():
    os.system('cls')
    for i in range(0, len(data)):
        print (data[i])
def getName():
    os.system('cls')
        #print(x for x, y in collections.Counter(data["points"]).items() if y > 1)



    values= []

    for value in data:
        #list_points.append(value["attendance"])
        #list_attendance.append(value["attendance"])
        #list_names.append(value["names"])
        #values.append(value['name']+str(value['points']/value['attendance']))
        for value2 in data:
            #print(value['name'] + ": " + str(value['points']/value['attendance']) + "\t" + value2['name'] + ": " +str(value['points']/value['attendance']))
            first_value = value['points']/value['attendance']
            second_value = value2['points']/value2['attendance']
            if (first_value <= second_value) & (value['name'] != value2['name']):
                selection = str(value['name'] + ": " + "with the value: " + str(value['points']/value['attendance']))

    print(selection)






















