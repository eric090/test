import data
info = []


class Users(object):

    def __init__(self, name, points, attendance, rate):

        self.name = name
        self.points = points
        self.attendance = attendance
        self.rate = rate
        a = {'name': self.name, 'attendance': self.attendance, 'points': self.points, 'rate': self.rate}
        info.clear()
        info.append(data.loadFile())
        if self.checkUser():
            info.append(a)
            data.saveFile(info)

    def getNames(self):

        self.getInfo("names")

    def getPoints(self, n_name):

        self.name = n_name
        n_points = self.getInfo("points")
        return n_points

    def getAttendances(self):
        self.getInfo("attendances")

    def getRates(self):
        self.getInfo("rates")

    def getInfo(self, option):

        info.clear()
        info.append(data.loadFile())
        print("info contiene: " + str(info))
        for value in info:
            if self.name == value['name']:
                if option == "points":
                    points = value['points']
                    return str(points)
                elif option == "attendances":
                    return value['attendance']
                elif option == "rats":
                    return value['rats']

    def checkUser(self):

        duplicateName = True
        n_name = self.name
        for value in info:
            print(value)
            if n_name == value['name']:
                print("esta repetido")
                duplicateName = False
                return duplicateName
        if duplicateName:
            print("no esta repetido")
            return True

# class User:
#
#     def getPoint(self):
#         self.getInfo(self.n_name, "point")
#
#     def getAttendance(self, name):
#         self.getInfo(name, "attendance")
#
#     def getRate(self, name):
#         self.getInfo(name)
#
#     def getInfo(self, name, option):
#         info = data.loadFile()
#         for value in info:
#             if name == "name":
#                 if option == "point":
#                     # return value['points']
#                     print(str(value["points"]))
#                 elif option == "attendance":
#                     # return value['attendance']
#                     print(str(value["attendance"]))
#                 elif option == "rate":
#                     # return value['attendance']
#                     print(str(value["rate"]))
