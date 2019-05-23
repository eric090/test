import data
info = []

class User(object):

    def __init__(self, name, birthdate, userid):
        self._name = name
        self._userid = userid
        self._birthdate = birthdate
        self._attendances = 0
        self._times_cleaned = 0
    @staticmethod
    def createUser(data):
        new_user = User(data['name'], data['birthdate'], data['userid']) 
        new_user._attendances = data['attendances']
        new_user._times_cleaned = data['timescleaned']
        return new_user

    @property
    def name(self):
        return self._name

    @property
    def userid(self):
        return self._userid

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def attendaces(self):
        return self._attendances

    @property
    def timescleaned(self):
        return self._times_cleaned

    @property
    def getRates(self):
        return

    def toDict(self):
        return {'name': self._name, 'birthdate': self._birthdate, 'attendances': self._attendances, 'timescleaned': self._times_cleaned, 'userid': self._userid}

class Users(object):

    def __init__(self):
        self._users = []
        users_data = data.get_data()
        for user_data in users_data:
            new_user = User.createUser(user_data)
            self._users.append(new_user)

    def addUser(self, name, birthdate):
        new_user = User(name, birthdate, data.get_uid())
        data.save_user(new_user)
        return new_user

    def getUsersInfo(self):
        ret = []
        for user in self._users:
            ret.append(user.toDict())
        return ret
