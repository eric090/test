import pickle
import os.path
a = {'name': "NAME", 'attendance': "ATTENDANCE", 'points': "POINTS", 'rate': "RATE"}
def newFile():
    F = open('names.pkl', 'wb')
    F.close()


def saveFile(info):
    F = open('names.pkl', 'wb')
    pickle.dump(info, F)
    F.close()


def loadFile():
    # pickle.load(open('names.pkl', 'rb'))
    if os.path.isfile('names.pkl'):
        F = open('names.pkl', 'rb')
    else:
        print("file created")
        F = open('names.pkl', 'wb')
        F.close()
        F = open('names.pkl', 'rb')

    try:
        return pickle.load(F)

    except EOFError:
        return a

    F.close()
