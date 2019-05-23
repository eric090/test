import pickle
import os.path

FILENAME = 'names.pkl'

UID = 0


def get_data():
    if not os.path.isfile(FILENAME):
        pickle.dump({"uid": 0, "users": []}, open(FILENAME, 'wb'))
    try:
        ofile = open(FILENAME, 'rb')
        data = pickle.load(ofile)
        global UID
        UID = data['uid']
    # except Exception, ex:
    #   print "Exception: ", ex.message
    finally:
        ofile.close()
    return data['users']


def save_user(user):
    try:
        ofile = open(FILENAME, 'rb')
        data = pickle.load(ofile)
        ofile.close()
        data['users'].append(user.toDict())
        pickle.dump(data, open(FILENAME, 'wb'))
    # except Exception, ex:
    # print "Exception: ", ex.message
    finally:
        ofile.close()
    pickle.dump(data, open(FILENAME, 'wb'))


def get_uid():
    global UID
    UID += 1
    try:
        ofile = open(FILENAME, 'rb')
        data = pickle.load(ofile)
        ofile.close()
        data['uid'] = UID
        pickle.dump(data, open(FILENAME, 'wb'))
    except:
        pass
    finally:
        ofile.close()
    return UID
